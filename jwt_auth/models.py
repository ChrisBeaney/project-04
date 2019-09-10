from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class User(AbstractUser):
    # custom fields here...
    handicap = models.FloatField(null=True)

    # add this line... not sure what it does..
    objects = UserManager()
