from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import GameBoardRegister,GetGameBoard
from rest_framework.permissions import IsAuthenticated
from Palindrome.Palindrome import Palindrome
from Palindrome.models import GameBoard


class UpdateGameBoardByUsingGameId(generics.GenericAPIView):
    serializer_class = GameBoardRegister
    permission_classes = (IsAuthenticated,)

    def put(self, request, Id):
        try:
            book = GameBoard.objects.get(id=Id)
            gamestring = request.data.get('Game_String')
            book.Game_String = gamestring
            book.Palindrome = Palindrome(gamestring)
            book.save()
            memberData = GetGameBoard(book)
            
            return Response({'Message': 'Successful',
                             'Result': memberData.data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': False,
                             'HasError': True,
                             'Status': 400})
