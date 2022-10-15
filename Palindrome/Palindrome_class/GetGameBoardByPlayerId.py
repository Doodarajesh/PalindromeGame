from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import GetGameBoard
from rest_framework.permissions import IsAuthenticated
from Palindrome.models import GameBoard


class GetGameBoardByPlayerId(generics.GenericAPIView):
    serializer_class = GetGameBoard
    permission_classes = (IsAuthenticated,)

    def get(self, request, PlayerId):
        try:
            print(PlayerId)
            member = GameBoard.objects.filter(PalyerId_id=PlayerId)
            memberData = GetGameBoard(member,many=True)
            data = []
            for i in memberData.data:
                print(i)
                if i['Game_String'] == i['Palindrome']:
                    i['Result'] = "Win The Game"
                    data.append(i)
                else:
                    i['Result'] = "Loose The Game"
                    data.append(i)
            
            return Response({'Message': 'Successful',
                             'Result': data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': False,
                             'HasError': True,
                             'Status': 400})
