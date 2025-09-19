from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, TrainerViewSet, MemberViewSet

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
