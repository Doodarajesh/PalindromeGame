from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import Playerseralizer
from rest_framework.permissions import IsAuthenticated
from Palindrome.models import Player


class GetAllPlayers(generics.GenericAPIView):
    serializer_class = Playerseralizer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            member = Player.objects.all()
            memberData = Playerseralizer(member, many=True)
            
            return Response({'Message': 'Successful',
                             'Result': memberData.data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': False,
                             'HasError': True,
                             'Status': 400})
