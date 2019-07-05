from .models import *
from .serializers import *
from .serializers import CreateUsuarioSerializer, GetUpdateRemoveUsuarioSerializer, ListUsuarioSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.db import connection

class GetUser(ListAPIView):
    def get(self, request, *args, **kwargs):
        # try:
        user = Usuario.objects.get(pk=request.user.pk)
        serializer = GetUpdateRemoveUsuarioSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_404_NOT_FOUND)


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
    foregin_keys = ['owner']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_userclub ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = UserClub.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = UserClub.objects.raw("SELECT * FROM api_userclub;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_userclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_userclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_userclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RealClubModelViewSet(viewsets.ModelViewSet):
    serializer_class = RealClubSerializer
    queryset = RealClub.objects.all()
    foregin_keys = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_realclub ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = RealClub.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = RealClub.objects.raw("SELECT * FROM api_realclub;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_realclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_realclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_realclub WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PositionModelViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    foregin_keys = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_position ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Position.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Position.objects.raw("SELECT * FROM api_position;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_position WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_position WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_position WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlayerModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    foregin_keys = ['posittion']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_player ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Player.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Player.objects.raw("SELECT * FROM api_player;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_player WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_player WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_player WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RoundModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.all()
    foregin_keys = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_round ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Round.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Round.objects.raw("SELECT * FROM api_round;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_round WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_round WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_round WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MatchModelViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    foregin_keys = ['home_club', 'away_club']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_match ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Match.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Match.objects.raw("SELECT * FROM api_match;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_match WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_match WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_match WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FormationModelViewSet(viewsets.ModelViewSet):
    serializer_class = FormationSerializer
    queryset = Formation.objects.all()
    foregin_keys = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_formation ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Formation.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Formation.objects.raw("SELECT * FROM api_formation;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_formation WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_formation WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_formation WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StatModelViewSet(viewsets.ModelViewSet):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()
    foregin_keys = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_stat ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Stat.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Stat.objects.raw("SELECT * FROM api_stat;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_stat WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_stat WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_stat WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LeagueModelViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()
    foregin_keys = ['creator']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_league ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = UserClub.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = UserClub.objects.raw("SELECT * FROM api_league;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_league WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_league WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_league WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FMTPosModelViewSet(viewsets.ModelViewSet):
    serializer_class = FMTPosSerializer
    queryset = FMTPos.objects.all()
    foregin_keys = ['position', 'formation']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_fmtpos ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = League.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = League.objects.raw("SELECT * FROM api_fmtpos;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_fmtpos WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_fmtpos WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_fmtpos WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlayerStatsModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatsSerializer
    queryset = PlayerStats.objects.all()
    foregin_keys = ['player', 'stat', '_round']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_playerstats ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = PlayerStats.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = PlayerStats.objects.raw("SELECT * FROM api_playerstats;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_playerstats WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_playerstats WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_playerstats WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SquadModelViewSet(viewsets.ModelViewSet):
    serializer_class = SquadSerializer
    queryset = Squad.objects.all()
    foregin_keys = ['club', 'fmt', '_round']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_squad ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Squad.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Squad.objects.raw("SELECT * FROM api_squad;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_squad WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_squad WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_squad WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SelectedModelViewSet(viewsets.ModelViewSet):
    serializer_class = SelectedSerializer
    queryset = Selected.objects.all()
    foregin_keys = ['club', 'player', '_round']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_selected ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = Selected.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Selected.objects.raw("SELECT * FROM api_selected;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_selected WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_selected WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_selected WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ClubLeagueModelViewSet(viewsets.ModelViewSet):
    serializer_class = ClubLeagueSerializer
    queryset = ClubLeague.objects.all()
    foregin_keys = ['club', ' league']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_clubleague ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = ClubLeague.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = ClubLeague.objects.raw("SELECT * FROM api_clubleague;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_clubleague WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_clubleague WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_clubleague WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlayerPriceModelViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerPriceSerializer
    queryset = PlayerPrice.objects.all()
    foregin_keys = ['player', '_round']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        keys = []
        for key in serializer.data.keys():
            if key in self.foregin_keys:
                keys.append('{}_id'.format(key))
            else:
                keys.append('{}'.format(key))
        values = []
        for value in serializer.data.values():
            if isinstance(value, str):
                values.append("'{}'".format(value))
            else:
                values.append(str(value))

        keys = ', '.join(keys)
        values = ', '.join(values)
        query_raw = "INSERT INTO api_playerprice ({}) VALUES ({})".format(keys, values)
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        
        data = serializer.data
        data['id'] = PlayerPrice.objects.last().pk
        return Response(data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = PlayerPrice.objects.raw("SELECT * FROM api_playerprice;")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk, **kwargs):
        query_raw = "SELECT * FROM api_playerprice WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
            columns = [col[0].replace('_id','') if '_id' in col[0] else col[0] for col in cursor.description]
            instance = dict(zip(columns, cursor.fetchone()))
        if instance is []:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(instance)

    def destroy(self, request, pk, **kwargs):
        query_raw = "DELETE FROM api_playerprice WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        query_raw = "SELECT * FROM api_playerprice WHERE id = {}".format(pk)
        instance = []
        with connection.cursor() as cursor:
            cursor.execute(query_raw)
        if instance == []:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
