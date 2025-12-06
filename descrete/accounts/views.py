from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    pass   # 默认即可