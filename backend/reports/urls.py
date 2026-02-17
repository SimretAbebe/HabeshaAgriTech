from django.urls import path
from .views import ReportCreateView, ExpertResponseView

urlpatterns = [
    path('', ReportCreateView.as_view(), name='report_create'),
    path('respond/', ExpertResponseView.as_view(), name='expert_response'),
]
