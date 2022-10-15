from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import Playerseralizer
from rest_framework.permissions import IsAuthenticated
from Palindrome.models import Player


class PlayerDelete(generics.GenericAPIView):
    serializer_class = Playerseralizer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, PlayerId):
        try:
            book = Player.objects.get(id=PlayerId)
            book.delete()
            return Response({'Message': 'Successful',
                             'Result': "Member deleted successfuly",
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': True,
                             'HasError': True,
                             'Status': 400})
