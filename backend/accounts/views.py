from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

from django.contrib.auth import get_user_model
from .permissions import IsAdmin

User = get_user_model()

class VerifyExpertView(generics.UpdateAPIView):
    queryset = User.objects.filter(role='expert')
    permission_classes = [IsAdmin]

    def update(self, request, *args, **kwargs):
        user_to_verify = self.get_object()
        user_to_verify.is_verified = True
        user_to_verify.save()
        return Response({"message": f"Expert {user_to_verify.username} verified successfully."})
