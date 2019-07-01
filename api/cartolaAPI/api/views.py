from .models import *
from .serializers import *
from .serializers import CreateUsuarioSerializer, GetUpdateRemoveUsuarioSerializer, ListUsuarioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets

class ListCreateUsuarioAPIView(ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = CreateUsuarioSerializer

	def list(self, request, *args, **kwargs):
		params = request.GET
		if params:
			if 'email' in params:
				queryset = Usuario.objects.get(email=params['email'])
				usuarios = ListUsuarioSerializer(queryset)
		else:
			queryset = Usuario.objects.all()
			usuarios = ListUsuarioSerializer(queryset,many=True)

		return Response(usuarios.data)

class GetUpdateRemoveUsuarioAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Usuario.objects.all()
	serializer_class = GetUpdateRemoveUsuarioSerializer
	lookup_url_kwarg = 'id_usuario'
	http_method_names = [u'get', u'post', u'put',u'delete', u'head', u'options']

class UserClubModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserClubSerializer
    queryset = UserClub.objects.all()

class RealClubModelViewSet(viewsets.ModelViewSet):
    serializer_class = RealClubSerializer
    queryset = RealClub.objects.all()

class PositionModelViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

class PlayerModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class RoundModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.all()

class MatchModelViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

class FormationModelViewSet(viewsets.ModelViewSet):
    serializer_class = FormationSerializer
    queryset = Formation.objects.all()

class StatModelViewSet(viewsets.ModelViewSet):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()

class LeagueModelViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()

class FMTPosModelViewSet(viewsets.ModelViewSet):
    serializer_class = FMTPosSerializer
    queryset = FMTPos.objects.all()

class PlayerStatsModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatsSerializer
    queryset = PlayerStats.objects.all()

class SquadModelViewSet(viewsets.ModelViewSet):
    serializer_class = SquadSerializer
    queryset = Squad.objects.all()

class SelectedModelViewSet(viewsets.ModelViewSet):
    serializer_class = SelectedSerializer
    queryset = Selected.objects.all()

class ClubLeagueModelViewSet(viewsets.ModelViewSet):
    serializer_class = ClubLeagueSerializer
    queryset = ClubLeague.objects.all()

class PlayerPriceModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerPriceSerializer
    queryset = PlayerPrice.objects.all()
