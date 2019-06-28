from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.compat import authenticate
from rest_framework.serializers import ModelSerializer, ValidationError, raise_errors_on_nested_writes
from rest_framework import serializers
from models import Usuario
from rest_framework.utils import model_meta
import re
from django.contrib.auth.password_validation import validate_password


class AuthTokenSerializer(serializers.Serializer):
	email = serializers.CharField(label=_("Email"),required=True)
	password = serializers.CharField(
		label=_("Password"),
		style={'input_type': 'password'},
		trim_whitespace=False,
		required=True
	)

	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')

		if email and password:
			user = authenticate(request=self.context.get('request'),
								email=email, password=password)
			if not user:
				msg = _('Unable to log in with provided credentials.')
				raise serializers.ValidationError(msg, code='authorization')
		else:
			msg = _('Must include "email" and "password".')
			raise serializers.ValidationError(msg, code='authorization')

		attrs['user'] = user
		return attrs


class CreateUsuarioSerializer(ModelSerializer):
    tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO)
    class Meta:
        model = Usuario
        fields = ('id','nome','cpf_cnpj','email','password','tipo_usuario')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(
            email = validated_data['email'],
            nome = validated_data['nome'],
            cpf_cnpj = validated_data['cpf_cnpj'],
            tipo_usuario = validated_data['tipo_usuario']
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def validate_cpf_cnpj(self,cpf_cnpj):
        if Usuario.objects.filter(cpf_cnpj = cpf_cnpj).exists():
            raise ValidationError('CPF/CNPJ já cadastrado!')

        if len(cpf_cnpj) < 11 or len(cpf_cnpj) > 14:
            raise ValidationError('CPF/CNPJ inválido!')

        if not cpf_cnpj.isdigit():
            raise ValidationError('CPF/CNPJ inválido!')

        return cpf_cnpj

    def validate_nome(self,nome):
        if bool(re.search(r'\d',nome)):
            raise ValidationError('Nome inválido!')

        if bool(re.search('[!-@[-_]',nome)):
            raise ValidationError('Nome inválido!')

        return nome

    def validate_tipo_usuario(self, tipo_usuario):
        if tipo_usuario != 'FISICA' and tipo_usuario != 'JURIDICA':
            raise ValidationError('Tipo de Usuario inválido!')
        return tipo_usuario


class ListUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nome','email','cpf_cnpj','telefone','endereco','foto',,'is_admin')


class GetUpdateRemoveUsuarioSerializer(CreateUsuarioSerializer):
    nome = serializers.CharField(required=False, max_length=255, allow_blank=False)
    email = serializers.CharField(required=True,max_length=255, allow_blank=False)
    telefone = serializers.CharField(required=False, max_length=14, allow_blank=False)
    endereco = serializers.CharField(required=False, max_length=350, allow_blank=False)
    foto = serializers.ImageField(required=False, allow_empty_file=False, use_url=True)
    first_access = serializers.BooleanField(required=False)
    new_password = serializers.CharField(required=False,style={'input_type': 'password'},allow_blank=True,default='')

    class Meta:
        model = Usuario
        fields = ('id','nome','telefone','email','endereco','cpf_cnpj', 'foto','new_password','first_access')
        extra_kwargs = {'email':{'write_only':True},
                        'new_password':{'write_only':True},
                        'cpf_cnpj':{'read_only':True}}

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        if 'new_password' in self.initial_data.keys():
            if validated_data['new_password']!='':
                instance.set_password(validated_data['new_password'])
        instance.save()

        return instance

    def to_representation(self, obj):
        return {
            'id':obj.id,
            'nome': obj.nome,
            'email':obj.email,
            'cpf_cnpj': obj.cpf_cnpj,
            'is_admin':obj.is_admin,
            'telefone': obj.telefone,
            'endereco': obj.endereco,
            'foto': obj.foto.url if obj.foto else None,
            'last_login':obj.last_login,
            'first_access':obj.first_access
        }