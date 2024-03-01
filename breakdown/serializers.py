from rest_framework import serializers
from . import models
from datetime import timedelta
from .models import Andon


class BreakdownCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BreakdownCategory
        fields = '__all__'

# class ShiftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Shift
#         fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'

class ShopfloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shopfloor
        fields = '__all__'

class AssemblylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assemblyline
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):   
    class Meta:
        model = models.Machine
        fields = '__all__'

class AndonSerializer(serializers.ModelSerializer):
    andon_alerts = serializers.DateTimeField(allow_null=True, required=False)
    andon_acknowledge = serializers.DateTimeField(allow_null=True, required=False)
    andon_resolved = serializers.DateTimeField(allow_null=True, required=False)
    total_time = serializers.SerializerMethodField()
    class Meta:
        model = Andon
        fields = (
                  'company',
                  'location',
                  'shopfloor',
                  'assemblyline',
                  'machineId',
                  'ticket',
                  'category',
                  'sub_category',
                  'alert_shift',
                  'andon_alerts',
                  'andon_acknowledge',
                  'andon_resolved',
                  'total_time') 

        
    def get_total_time(self, obj):
        andon_alerts = obj.andon_alerts
        andon_resolved = obj.andon_resolved

        if andon_alerts and andon_resolved:
            time_difference = andon_resolved - andon_alerts
            total_seconds = time_difference.total_seconds()
            total_time = str(timedelta(seconds=total_seconds))
            return total_time

        return "00:00"
    


class BreakdownHmiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BreakdownHMI
        fields = '__all__'


class AndonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AndonData
        fields = '__all__'


