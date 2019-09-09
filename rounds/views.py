from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.response import Response # get the Response class from DRF

from .models import Round #Hole
from .serializers import RoundSerializer # HoleSerializer, CourseSerializer, NestedHoleSerializer, NestedCourseSerializer # get the HoleSerializer

# Create your views here.
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


class RoundList(APIView):

    def get(self, _request):
        rounds = Round.objects.all()
        serializer = RoundSerializer(rounds, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status="201")

        return Response(serializer.errors, status="422")
