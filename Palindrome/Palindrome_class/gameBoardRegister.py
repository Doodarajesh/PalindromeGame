from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import GameBoardRegister,GetGameBoard
from rest_framework.permissions import IsAuthenticated


class GameBoardRegister(generics.GenericAPIView):
    serializer_class = GameBoardRegister
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            
            return Response({'Message': 'Successful',
                             'Result': GetGameBoard(user).data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': True,
                             'HasError': True,
                             'Status': 400})
