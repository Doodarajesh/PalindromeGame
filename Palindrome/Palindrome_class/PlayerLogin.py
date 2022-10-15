from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import PlayerLogin,Playerseralizer
from Palindrome.models import Player
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password


class PlayerLogin(generics.GenericAPIView):
    serializer_class = PlayerLogin
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('Username')      
            password = request.data.get('Password') 
            user = Player.objects.get(Username=username)    
            if check_password(password,user.Password):
                return Response({'Message': 'Successful',
                                'Result': Playerseralizer(user).data,
                                'HasError': False,
                                'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': True,
                             'HasError': True,
                             'Status': 400})