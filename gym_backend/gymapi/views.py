# Create your views here.
from rest_framework import viewsets
from .models import Plan, Trainer, Member
from .serializers import PlanSerializer, TrainerSerializer, MemberSerializer

# CRUD for Plans
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# CRUD for Trainers
class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

# CRUD for Members
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer





