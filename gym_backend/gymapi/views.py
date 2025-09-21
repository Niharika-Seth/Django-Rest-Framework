# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import Plan, Trainer, Member
from .serializers import PlanSerializer, TrainerSerializer, MemberSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer




