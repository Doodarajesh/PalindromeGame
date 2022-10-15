from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *
from .Palindrome import Palindrome


class Playerseralizer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','Firstname','Lastname','Username','mobileNumber']


class PlayerRegister(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['Firstname','Lastname','Username','Password','mobileNumber']
    def create(self, validated_data):
        user = Player.objects.create(Firstname=validated_data['Firstname'],
                                            Lastname=validated_data['Lastname'],
                                            Username=validated_data['Username'], 
                                            Password=make_password(validated_data['Password']),
                                            mobileNumber=validated_data['mobileNumber'])
        user.save()
        return user


class GameBoardRegister(serializers.ModelSerializer):
    class Meta:
        model = GameBoard
        fields = ['PalyerId','Game_String']
    def create(self, validated_data):
        user = GameBoard.objects.create(PalyerId=validated_data['PalyerId'],
                                            Game_String=validated_data['Game_String'],
                                            Palindrome=Palindrome(validated_data['Game_String']))
        user.save()
        return user


class GetGameBoard(serializers.ModelSerializer):
    PalyerId = Playerseralizer(read_only=True)
    class Meta:
        model = GameBoard
        fields = ['PalyerId','Game_String','Palindrome']



class PlayerLogin(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['Username','Password']
    