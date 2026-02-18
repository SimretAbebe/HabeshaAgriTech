from rest_framework import generics
from .models import Report
from .serializers import ReportSerializer
from accounts.permissions import IsFarmer, IsVerifiedExpert
from rest_framework.response import Response

class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsFarmer]

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)

class ExpertResponseView(generics.CreateAPIView):
    # Dummy view to test IsVerifiedExpert permission
    permission_classes = [IsVerifiedExpert]

    def create(self, request, *args, **kwargs):
        return Response({"message": "Expert response submitted successfully."})
