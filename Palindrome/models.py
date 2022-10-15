from email.policy import default
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Player(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Username = models.CharField(max_length=244, unique=True)
    Password = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    mobileNumber = models.CharField(validators=[phone_regex], max_length=10)

    class Meta:
        db_table = "Players"


class GameBoard(models.Model):
    PalyerId = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='Player')
    Game_String = models.CharField(max_length=6,default=True,null=True)
    Palindrome = models.CharField(max_length=6)

    class Meta:
        db_table = "GameBoard"

