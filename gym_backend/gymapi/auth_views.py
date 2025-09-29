# gymapi/auth_views.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([AllowAny])  # allow unauthenticated login
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # creates session
        return Response({"message": "Login successful"}, status=200)
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(["POST"])
def user_logout(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=200)
