from rest_framework import generics
from rest_framework.response import Response
import json
from Palindrome.serializers import PlayerRegister,Playerseralizer
from rest_framework.permissions import IsAuthenticated


class PlayerRegister(generics.GenericAPIView):
    serializer_class = PlayerRegister
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        '''Player register'''
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            
            return Response({'Message': 'Successful',
                             'Result': Playerseralizer(user).data,
                             'HasError': False,
                             'Status': 200})
        except Exception as e:
            return Response({'Message': str(e),
                             'Result': True,
                             'HasError': True,
                             'Status': 400})
