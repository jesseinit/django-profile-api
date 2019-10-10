from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import serializers, models, permissions


class HelloAPIView(APIView):
    """ Test API View """

    # Define serializer fot this view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = ['Uses HTTP Methods as Functions(get,post,patch,delete)',
                      'Gives you the most control over your application logic',
                      'is mapped manually to URLS']
        return Response({'message': 'Hello 😜😜😜', 'an_apiview': an_apiview})

    def post(self, request,):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object """
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """ Handles patching an object """
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """ Handles deleting an object """
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Returns a hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles retrieval of an object by its ID """
        return Response({'message': f'Retrieved {pk}'})

    def update(self, request, pk=None):
        """ Handles updating an object """
        return Response({'message': 'UPDATE'})

    def destroy(self, request, pk=None):
        """ Handles removing an object """
        return Response({'message': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handles creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles crating, reading and updating profile feed items """
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, permissions.UpdateOwnStatus)

    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
