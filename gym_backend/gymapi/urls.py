# gymapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, TrainerViewSet, MemberViewSet
from . import auth_views

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Auth endpoints
    path('auth/login/', auth_views.user_login, name='api_login'),
    path('auth/logout/', auth_views.user_logout, name='api_logout'),
]




