from .models import Usuario
from .serializers import CreateUsuarioSerializer, GetUpdateRemoveUsuarioSerializer, ListUsuarioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

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