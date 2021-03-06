from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.conf import settings
# from jwt_auth.models import User
# from django_mysql.models import ListCharField
# from django.contrib.postgres.fields import ArrayField # Not sure if this works with sqlite


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # par = models.IntegerField()

    @property
    def par(self):
        return sum([hole.par for hole in self.holes.all()])

    def __str__(self):
        return f'{self.name}'


class Hole(models.Model):
    number = models.IntegerField()
    par = models.IntegerField(default=4, validators=[MaxValueValidator(5), MinValueValidator(3)])
    stroke_index = models.IntegerField(default=9, validators=[MaxValueValidator(18), MinValueValidator(1)])
    yards = models.IntegerField(default=350)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        related_name='holes'
    )

    def __str__(self):
        return f'{self.course} - Hole: {self.number}'


class Score(models.Model):
    date = models.DateField(default=timezone.now)
    shots = models.IntegerField(default=4)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scores')
    hole = models.ForeignKey(
        Hole,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.hole} - Score: {self.shots}'


# class Player(models.Model):
#     name = models.CharField(max_length=50)
#     handicap = models.FloatField()
#     playing_handicap = models.IntegerField(blank=True, null=True)
#
#     def round_handicap(self):
#         self.playing_handicap = round(self.handicap)
#         return round(self.playing_handicap)
#
#     def __str__(self):
#         return f'{self.name} - handicap (playing): {self.handicap} ({self.round_handicap()})'


# class Round(models.Model):
#     played_date = models.DateField(default=timezone.now)
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.SET_NULL,
#         null=True,
#     )
#     player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # user = models.ForeignKey(User, related_name='rounds', on_delete=models.CASCADE)
#
#     # May not need this line.
#     scores = ListCharField(base_field=models.IntegerField(), max_length=255, size=18, blank=True)
#     # scores = ArrayField(base_field=models.IntegerField(), size=18)
#
#     def __str__(self):
#         return f'Round at {self.course} on {self.played_date} created.'
