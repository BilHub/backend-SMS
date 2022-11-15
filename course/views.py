from rest_framework.viewsets import ModelViewSet

from .models import Subject, Level, Cycle
from .serializers import SubjectSerializer, LevelSerializer, CycleSerializer

class CycleViewSet(ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    filterset_fields = ["cycle_id"]

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_fields = ["level_id", "cycle_id"]


    