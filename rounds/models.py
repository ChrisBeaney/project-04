from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    par = models.IntegerField()

    def __str__(self):
        return f'{self.name}: par - {self.par}'


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
        return round(self.handicap)

    def __str__(self):
        return f'{self.name} - handicap(playing): {self.handicap}({self.round_handicap()})'


class Score(models.Model):
    shots = models.IntegerField()
