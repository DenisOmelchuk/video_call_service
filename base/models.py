from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    role = models.CharField(max_length=25, null=True)
    alive = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['avatar']


# class RoomMember(models.Model):
#     name = models.CharField(max_length=200)
#     uid = models.CharField(max_length=200)
#     room_name = models.CharField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.name
    

class GameRoom(models.Model):
    necessary_number_of_players = models.IntegerField()
    players = models.ManyToManyField(User, related_name='players', blank=True)
    room_name = models.CharField(max_length=200, blank=True, null=True)
    # game_started = models.BooleanField(default=False)
    # game_started_time = models.DateTimeField(blank=True, null=True)
    # current_round = models.IntegerField(default=0)

    def __str__(self):
        return self.room_name



    
