from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    par = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Hole(models.Model):
    number = models.IntegerField()
    par = models.IntegerField(default=4, validators=[MaxValueValidator(5), MinValueValidator(3)])
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f'{self.course} - Hole: {self.number}'


class Player(models.Model):
    name = models.CharField(max_length=50)
    handicap = models.FloatField()
    playing_handicap = models.IntegerField(blank=True, null=True)

    def round_handicap(self):
        self.playing_handicap = round(self.handicap)
        return round(self.playing_handicap)

    def __str__(self):
        return f'{self.name} - handicap (playing): {self.handicap} ({self.round_handicap()})'


class Score(models.Model):
    shots = models.IntegerField(default=4)
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    hole = models.ForeignKey(
        Hole,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.hole} - Score: {self.shots}'


class Round(models.Model):
    # course = models.ForeignKey(
    #     Course,
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )
    # player = models.ForeignKey(
    #     Player,
    #     on_delete=models.CASCADE
    # )
    played_date = models.DateField(default=timezone.now)
