# Creating serializers
from rest_framework import serializers
from .models import Member, Plan, Trainer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'duration_months']

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'specialization', 'experience_years']

class MemberSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'join_date', 'plan', 'trainer']




