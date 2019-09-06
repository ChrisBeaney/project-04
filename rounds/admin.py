from django.contrib import admin
from .models import Course, Hole, Player, Score, Round

# Register your models here.
admin.site.register(Course)
admin.site.register(Hole)
admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Round)
