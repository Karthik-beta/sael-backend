from rest_framework import serializers
from report import models


class productionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.productionReport
        fields = '__all__'