from rest_framework import serializers
from jwt_auth.serializers import UserSerializer
from .models import Course, Hole, Round, Score


class NestedCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'par')


class NestedHoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'course')


class NestedRoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = ('id', 'played_date', 'course', 'player', 'scores')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'par')


class HoleSerializer(serializers.ModelSerializer):

    course = NestedCourseSerializer()

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'course')


class RoundSerializer(serializers.ModelSerializer):

    course = NestedCourseSerializer()
    player = UserSerializer()

    class Meta:
        model = Round
        fields = ('id', 'played_date', 'course', 'player', 'scores')


class ScoreSerializer(serializers.ModelSerializer):

    player = UserSerializer()
    hole = NestedHoleSerializer()
    round = NestedRoundSerializer()

    class Meta:
        model = Score
        fields = ('id', 'shots', 'player', 'hole', 'round')
