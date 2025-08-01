from rest_framework.generics import ListCreateAPIView
from .models import Cricketer
from .serializers import CricketerSerializer
from rest_framework import viewsets


class CricketerListCreateView(ListCreateAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer

class CricketerViewSet(viewsets.ModelViewSet):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer