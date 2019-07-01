from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class UsuarioManager(BaseUserManager):
	def create_user(self, **kwargs):

		if not 'name' in kwargs:
			raise ValueError('O name é obrigatório')

		if not 'email' in kwargs:
			raise ValueError('O Email é obrigatório!')

		if not 'password' in kwargs:
			raise ValueError('A senha é obrigatória!')

		user = self.model(
			email=self.normalize_email(kwargs['email']),
			name=kwargs['name']
		)

		user.set_password(kwargs['password'])
		user.save(using=self._db)
		return user

	def create_superuser(self, name, email, password):
		user = self.create_user(
			email=email,
			password=password,
			name=name,
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

	name = models.CharField(max_length=255)
	birthdate = models.DateField(auto_now=False,null=True, blank=True)
	foto = models.ImageField(upload_to="fotos/uploads", blank=True,null=True)

	is_active = models.BooleanField(default=True)
	first_access = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)


	objects = UsuarioManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

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

class UserClub(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    color1 = models.CharField(max_length=7, default='#FF0000', null=True, blank=True)
    color2 = models.CharField(max_length=7, default='#FFFFFF', null=True, blank=True)
    color3 = models.CharField(max_length=7, default='#000000', null=True, blank=True)
    crest = models.ImageField(upload_to="fotos/crest", blank=True,null=True)
    owner = models.ForeignKey("Usuario", on_delete=models.SET_NULL, null=True, blank=True)

class RealClub(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    crest = models.ImageField(upload_to="fotos/crest", blank=True,null=True)
    short_name = models.CharField(max_length=3, null=True, blank=True)

class Position(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    cod_pos = models.CharField(max_length=3, null=True, blank=True)

class Player(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    club = models.ForeignKey(RealClub, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)

class Round(models.Model): 
    round_number = models.IntegerField(null=True, blank=True)
    season = models.IntegerField(null=True, blank=True)

class Match(models.Model):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)
    home_club = models.ForeignKey(RealClub, on_delete=models.SET_NULL, null=True, blank=True, related_name='home_club')
    away_club = models.ForeignKey(RealClub, on_delete=models.SET_NULL, null=True, blank=True, related_name='away_club')
    _round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, blank=True)

class Formation(models.Model):
    nome = models.CharField(max_length=5, null=True, blank=True)

class Stat(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    desc = models.CharField(max_length=300, null=True, blank=True)
    points = models.DecimalField(decimal_places=2, max_digits=5,null=True, blank=True)


class League(models.Model):
    color1 = models.CharField(max_length=7, default='#FF0000', null=True, blank=True)
    color2 = models.CharField(max_length=7, default='#FFFFFF', null=True, blank=True)
    color3 = models.CharField(max_length=7, default='#000000', null=True, blank=True)
    crest = models.ImageField(upload_to="fotos/crest", blank=True,null=True)
    creator = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

class FMTPos(models.Model):
    amount = models.IntegerField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True, blank=True)

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    stat = models.ForeignKey(Stat, on_delete=models.SET_NULL, null=True, blank=True)
    _round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, blank=True)

class Squad(models.Model):
    club = models.ForeignKey(UserClub, on_delete=models.SET_NULL, null=True, blank=True)
    fmt = models.ForeignKey(FMTPos, on_delete=models.SET_NULL, null=True, blank=True)
    _round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, blank=True)

class Selected(models.Model):
    club = models.ForeignKey(UserClub, on_delete=models.SET_NULL, null=True, blank=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    _round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, blank=True)

class ClubLeague(models.Model):
    club = models.ForeignKey(UserClub, on_delete=models.SET_NULL, null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)

class PlayerPrice(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    _round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    captain = models.SmallIntegerField(null=True, blank=True)