from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.response import Response # get the Response class from DRF
# from .permissions import IsOwnerOrReadOnly
from jwt_auth.serializers import UserSerializer
from .models import Course, Hole, Score
from .serializers import NestedCourseSerializer, NestedHoleSerializer, CourseSerializer, HoleSerializer, ScoreSerializer


# Create your views here.
class CourseListView(APIView):
    def get(self, _request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status="422")


class CourseDetailView(APIView):
    def get(self, _request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class ScoreListView(APIView):
    def get(self, _request):
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status="201")
        return Response(serializer.errors, status="422")


class ProfileView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)



# class ListView(APIView): # extend the APIView
#
#     def get(self, _request):
#         holes = Hole.objects.all() # get all the holes
#         serializer = NestedHoleSerializer(holes, many=True)
#
#         return Response(serializer.data) # send the JSON to the client
#
#
# class DetailView(APIView): # extend the APIView
#
#     def get(self, _request, pk):
#         hole = Hole.objects.get(pk=pk) # get a hole by id (pk means primary key)
#         serializer = HoleSerializer(hole)
#
#         return Response(serializer.data) # send the JSON to the client
