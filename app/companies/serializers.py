from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'city',
            'start_date',
            'created_at'
        ]