from rest_framework import serializers
from jwt_auth.serializers import UserSerializer
from .models import Course, Hole, Score


class NestedCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'par')


class NestedHoleSerializer(serializers.ModelSerializer):

    course = NestedCourseSerializer()

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'stroke_index', 'course', 'yards',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'par',)


class HoleSerializer(serializers.ModelSerializer):

    course = NestedCourseSerializer()

    class Meta:
        model = Hole
        fields = ('id', 'number', 'par', 'stroke_index', 'course')


class PopulatedCourseSerializer(serializers.ModelSerializer):

    holes = NestedHoleSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'par', 'holes')


class ScoreSerializer(serializers.ModelSerializer):

    # player = UserSerializer()
    # hole = NestedHoleSerializer(read_only=True)

    class Meta:
        model = Score
        fields = ('id', 'date', 'shots', 'hole', 'player')

class PopulatedScoreSerializer(ScoreSerializer):

    hole = NestedHoleSerializer(read_only=True)



class PopulatedUserSerializer(UserSerializer):

    scores = PopulatedScoreSerializer(many=True)

    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'email', 'scores', 'handicap',)

# class NestedRoundSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Round
#         fields = ('id', 'played_date', 'course', 'player', 'scores')


# class RoundSerializer(serializers.ModelSerializer):
#
#     course = NestedCourseSerializer()
#     player = UserSerializer()
#
#     class Meta:
#         model = Round
#         fields = ('id', 'played_date', 'course', 'player', 'scores')
