from rest_framework.views import APIView # get the APIView class from DRF
from rest_framework.response import Response # get the Response class from DRF

from .models import Hole
from .serializers import HoleSerializer, CourseSerializer, NestedHoleSerializer, NestedCourseSerializer # get the HoleSerializer

# Create your views here.
class ListView(APIView): # extend the APIView

    def get(self, _request):
        holes = Hole.objects.all() # get all the holes
        serializer = NestedHoleSerializer(holes, many=True)

        return Response(serializer.data) # send the JSON to the client


class DetailView(APIView): # extend the APIView

    def get(self, _request, pk):
        hole = Hole.objects.get(pk=pk) # get a hole by id (pk means primary key)
        serializer = HoleSerializer(hole)

        return Response(serializer.data) # send the JSON to the client
