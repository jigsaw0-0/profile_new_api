from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_apiview = [
            'Uses HTTP Methods as functions (get, post, put, patch, delete)',
            'Is similar to a tranditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
