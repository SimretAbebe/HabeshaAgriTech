from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    farmer_name = serializers.ReadOnlyField(source='farmer.username')

    class Meta:
        model = Report
        fields = ('id', 'title', 'description', 'farmer', 'farmer_name', 'created_at')
        read_only_fields = ('farmer',)
