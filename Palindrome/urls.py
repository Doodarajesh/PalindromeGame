from django.urls import path
from .views import *

urlpatterns = [
    path('PlayerRegister/', PlayerRegister.as_view(),name='Player register'),
    path('PlayerLogin/', PlayerLogin.as_view(), name='Player can Register the Members'),
    path('GameBoardRagister/',GameBoardRegister.as_view(),name='Game board Register'),
    path('PlayersGet/',GetAllPlayers.as_view(), name='Get all player'),
    path('GetThePlayerId/<int:PlayerId>/',GetPlayerByUsingPlayerId.as_view(), name='Get the Player by using PlayerId'),
    path('GetGameBoardByPlayerId/<int:PlayerId>/',GetGameBoardByPlayerId.as_view(),name='get the gameboard by using playerId'),
    path('UpdateTheGameBoard/<int:Id>/',UpdateGameBoardByUsingGameId.as_view(),name='update the GameBoard'),
    path('PlayerDelete/<int:PlayerId>/',PlayerDelete.as_view(),name='Player delete')
]