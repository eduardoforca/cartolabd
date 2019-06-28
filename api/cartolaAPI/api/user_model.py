from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class UsuarioManager(BaseUserManager):
	def create_user(self, **kwargs):

		if not 'nome' in kwargs:
			raise ValueError('O nome é obrigatório')

		if not 'email' in kwargs:
			raise ValueError('O Email é obrigatório!')

		if not 'password' in kwargs:
			raise ValueError('A senha é obrigatória!')

		if not 'cpf_cnpj' in kwargs:
			raise ValueError('O CPF é obrigatório!')

		user = self.model(
			email=self.normalize_email(kwargs['email']),
			nome=kwargs['nome'],
			cpf_cnpj=kwargs['cpf_cnpj']
		)

		user.set_password(kwargs['password'])
		user.save(using=self._db)
		return user

	def create_superuser(self, nome, email, password):
		user = self.create_user(
			email=email,
			password=password,
			nome=nome,
			cpf_cnpj="12345678912"
		)
		user.is_admin = True
		user.first_access = True
		user.save(using=self._db)
		return user


class Usuario(AbstractBaseUser):

	email = models.EmailField(
		verbose_name='Endereço de Email',
		max_length=255,
		unique=True,
	)

	nome = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	first_access = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	telefone=models.CharField(max_length=14)
	cpf_cnpj=models.CharField(max_length=14)
	endereco=models.CharField(max_length=350)

	# True é Residencial, False é Empresa

	#tipo_usuario=models.BooleanField(default=True)

	foto = models.ImageField(upload_to="fotos/uploads", blank=True,null=True)


	objects = UsuarioManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome']

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):
		return str(self.id)+"-"+self.email

	def has_perm(self, perm, obj=None):
		"O usuário tem alguma permissão específica?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Tem permissão para ver o app_label?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"O usuário é membro de staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

	def is_first_access(self):
		return self.first_access
