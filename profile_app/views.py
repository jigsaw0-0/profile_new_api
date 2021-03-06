from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_app import serializers

from rest_framework import viewsets
from profile_app import models


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_apiview = [
            'Uses HTTP Methods as functions (get, post, put, patch, delete)',
            'Is similar to a tranditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})


    def post(self, request):
        """Add name to Hello """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle replacement of objects"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of objects"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSe"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, update, partial_update, delete etc)',
            'Automaticalls maps URLs using Routers',
            'More functionality at less code',
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hellow {name}!'

            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})



    def update(self, request, pk=None):
        """Handle updates"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """Delete object"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
