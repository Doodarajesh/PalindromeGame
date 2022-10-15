from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import Playerseralizer
from rest_framework.permissions import IsAuthenticated
from Palindrome.models import Player


class GetPlayerByUsingPlayerId(generics.GenericAPIView):
    serializer_class = Playerseralizer
    permission_classes = (IsAuthenticated,)

    def get(self, request, PlayerId):
        try:
            member = Player.objects.get(id=PlayerId)
            memberData = Playerseralizer(member)
            
            return Response({'Message': 'Successful',
                             'Result': memberData.data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': False,
                             'HasError': True,
                             'Status': 400})
