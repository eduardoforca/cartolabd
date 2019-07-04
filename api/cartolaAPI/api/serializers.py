from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError, raise_errors_on_nested_writes
from rest_framework import serializers
from .models import *
from rest_framework.utils import model_meta
import re
from django.conf import settings
from django.conf.urls.static import static


class CreateUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','name','email','password','foto','birthdate')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(
            email = validated_data['email'],
            name = validated_data['name'], 
            **validated_data
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def validate_name(self,name):
        if bool(re.search(r'\d',name)):
            raise ValidationError('name inválido!')

        if bool(re.search('[!-@[-_]',name)):
            raise ValidationError('name inválido!')

        return name


class ListUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','name','email','foto','birthdate')


class GetUpdateRemoveUsuarioSerializer(CreateUsuarioSerializer):
    name = serializers.CharField(required=False, max_length=255, allow_blank=False)
    birthdate = serializers.DateField(required=False)
    email = serializers.CharField(required=True,max_length=255, allow_blank=False)
    foto = serializers.ImageField(required=False, allow_empty_file=False, use_url=True)
    first_access = serializers.BooleanField(required=False)
    new_password = serializers.CharField(required=False,style={'input_type': 'password'},allow_blank=True,default='')

    class Meta:
        model = Usuario
        fields = ('id','name','email','foto','new_password','birthdate','first_access')
        extra_kwargs = {'email':{'write_only':True},
                        'new_password':{'write_only':True},
                        'first_access':{'read_only':True}}

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
            'name': obj.name,
            'email':obj.email,
            'birthdate': obj.birthdate,
            'is_admin':obj.is_admin,
            'foto': static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + obj.foto.url if obj.foto else None,
            'last_login':obj.last_login,
            'first_access':obj.first_access
        }

class UserClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClub
        fields = ('__all__')

class RealClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealClub
        fields = ('__all__')

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('__all__')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('__all__')

class RoundSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Round
        fields = ('__all__')

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('__all__')

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = ('__all__')

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('__all__')

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('__all__')

class FMTPosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FMTPos
        fields = ('__all__')

class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = ('__all__')

class SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = ('__all__')

class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selected
        fields = ('__all__')

class ClubLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubLeague
        fields = ('__all__')

class PlayerPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPrice
        fields = ('__all__')
