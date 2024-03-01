from rest_framework import serializers
from config import models


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.company
        fields = '__all__'

class plantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.plant
        fields = '__all__'

class shopfloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.shopfloor
        fields = '__all__'

class assemblylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.assemblyline
        fields = '__all__'

class machineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.machine
        fields = '__all__'

class batchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.batch
        fields = '__all__'

class poNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.poNo
        fields = '__all__'

class productReceipePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRecipe2
        # fields = ['id', 'product_Name', 'stages', 'target_per_unit', 'skill_matrix']
        fields = '__all__'

class productReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRecipe2
        fields = '__all__'

class attendanceRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.attendanceRules
        fields = '__all__'


class departmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.department
        fields = '__all__'


class designationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.designation
        fields = '__all__'
    

        
        
class QCDefectTypeSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.product_Name', read_only=True)
    parameter_name = serializers.CharField(source='parameter_id.parameter_name', read_only=True)

    class Meta:
        model = models.QCDefectType
        fields = ['id', 'product_id', 'product_name', 'parameter_id', 'parameter_name', 'defect_name', 'defect_code']
        
# class QCDefectTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.QCDefectType
#         fields = ['id', 'product_id', 'parameter_id', 'defect_name', 'defect_code']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         product_name = instance.product_id.product_Name
#         parameter_name = instance.parameter_id.parameter_name

#         nested_representation = {
#             'product_id': {
#                 'product_name': product_name,
#                 'parameter_id': {
#                     'parameter_name': parameter_name,
#                     'defect_name': representation['defect_name'],
#                     'defect_code': representation['defect_code']
#                 }
#             }
#         }

#         return nested_representation
        

# class QCDefectTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.QCDefectType
#         fields = ['id', 'product_id', 'parameter_id', 'defect_name', 'defect_code']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         product_name = instance.product_id.product_Name
#         parameter_name = instance.parameter_id.parameter_name

#         # Initialize the nested_representation variable
#         nested_representation = {
#             'product_name': {
#                 product_name: {
#                     'parameter_name': {
#                         parameter_name: []
#                     }
#                 }
#             }
#         }

#         # Update the nested_representation variable based on existing values
#         if product_name in nested_representation['product_name'] and parameter_name in nested_representation['product_name'][product_name]['parameter_name']:
#             nested_representation['product_name'][product_name]['parameter_name'][parameter_name].append({
#                 'defect_name': representation['defect_name'],
#                 'defect_code': representation['defect_code']
#             })
#         else:
#             nested_representation['product_name'][product_name]['parameter_name'][parameter_name] = [{
#                 'defect_name': representation['defect_name'],
#                 'defect_code': representation['defect_code']
#             }]

#         return nested_representation


class InspectionParameterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.InspectionParameters
        fields = '__all__'

class ShiftTimingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ShiftTiming
        fields = '__all__'


