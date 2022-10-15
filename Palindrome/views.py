from django.shortcuts import render
from Palindrome.Palindrome_class.PlayerRegister import PlayerRegister
from Palindrome.Palindrome_class.PlayerLogin import PlayerLogin
from Palindrome.Palindrome_class.gameBoardRegister import GameBoardRegister
from Palindrome.Palindrome_class.PlayerDelete import PlayerDelete
from Palindrome.Palindrome_class.GetAllPlayer import GetAllPlayers
from Palindrome.Palindrome_class.GetThePlayerByUsingId import GetPlayerByUsingPlayerId
from Palindrome.Palindrome_class.GetGameBoardByPlayerId import GetGameBoardByPlayerId
from Palindrome.Palindrome_class.UpdateTheGameBoardbygameId import UpdateGameBoardByUsingGameId

PlayerRegister()
PlayerLogin()
GameBoardRegister()
GetAllPlayers()
GetPlayerByUsingPlayerId()
GetGameBoardByPlayerId()
UpdateGameBoardByUsingGameId()
PlayerDelete()

# Create your views here.
