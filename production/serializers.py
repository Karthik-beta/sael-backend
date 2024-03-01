from rest_framework import serializers
from production import models



class productionPlanningSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.productionPlanning
        fields = '__all__'
    
class recentOrdersSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = models.productionPlanning
        fields = ['product_id', 'customer', 'status']

    def get_status(self, instance):
        if instance.assigned_date and not instance.planned_date and not instance.processing_date and not instance.completed_date:
            return "New"
        elif instance.assigned_date and instance.planned_date and not instance.processing_date and not instance.completed_date:
            return "Planned"
        elif instance.assigned_date and instance.planned_date and instance.processing_date and not instance.completed_date:
            return "Processing"
        elif instance.assigned_date and instance.planned_date and instance.processing_date and instance.completed_date:
            return "Completed"
        else:
            return "Unknown"



class productionPlanningPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.productionPlanning
        fields = ('product_id', 'customer', 'po_no', 'batch_no', 'quantity', 'expected_date')

class openJobWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.productionPlanning
        fields = ('id', 'job_id')

class lineMachineConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.lineMachineConfig
        fields = '__all__'


class lineMachineSlotConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.lineMachineSlotConfig
        fields = '__all__'

class ScheduleInputSerializer(serializers.Serializer):
    job_id = serializers.CharField()
    company = serializers.CharField()
    plant = serializers.CharField()
    shopfloor = serializers.CharField()
    assembly_line = serializers.CharField()
    machine_id = serializers.CharField()
    product_id = serializers.CharField()
    quantity = serializers.IntegerField()
    start_date = serializers.DateField()
    # product_target = serializers.CharField()
    # start_shift = serializers.CharField()
    # start_time = serializers.CharField()


class machineWiseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.machineWiseData
        fields = '__all__'


class machineWiseDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.machineWiseData
        fields = ('date', 'time', 'on_time', 'actual')


class AssemblyLineWiseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.assemblyLineWiseData
        fields = '__all__'

class soloAssemblyLineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.soloAssemblyLineData
        fields = '__all__'

class soloAssemblyLineDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.soloAssemblyLineData
        fields = ('mc_on_hours', 'actual', 'target', 'current')


class spellAssemblyLineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.spellAssemblyLineData
        fields = '__all__'

class spellAssemblyLineDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.spellAssemblyLineData
        fields = ('mc_on_hours', 'actual', 'target', 'current')


class ProductionAndonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductionAndon
        fields = '__all__'