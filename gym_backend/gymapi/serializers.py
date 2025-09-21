from rest_framework import serializers
from .models import Member, Plan, Trainer

# Plan Serializer
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'duration_months']

# Trainer Serializer
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'specialization', 'experience_years']

# Member Serializer (nested plan & trainer)
class MemberSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    trainer = TrainerSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all(), source='plan', write_only=True)
    trainer_id = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all(), source='trainer', write_only=True, allow_null=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'join_date', 'plan', 'trainer', 'plan_id', 'trainer_id']


