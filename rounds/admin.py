from django.contrib import admin
from .models import Course, Hole, Score

# Register your models here.
admin.site.register(Course)
admin.site.register(Hole)
admin.site.register(Score)
