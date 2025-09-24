from rest_framework import viewsets
from .models import Zoo
from .serializers import ZooSerializer

class ZooViewSet(viewsets.ModelViewSet):
    queryset = Zoo.objects.all()
    serializer_class = ZooSerializer
