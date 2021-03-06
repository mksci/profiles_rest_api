from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    "Test API View"

    def get(self, request, format=None):
        "Returns a list of APIVIew features"
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
