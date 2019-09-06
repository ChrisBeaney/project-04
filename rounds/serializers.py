from rest_framework import serializers
from .models import Hole, Course


class NestedCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'par')


class NestedHoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'course')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model: Course
        fields = ('id', 'name', 'par')


class HoleSerializer(serializers.ModelSerializer):

    course = NestedCourseSerializer()

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'course')
