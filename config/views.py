from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, F, Value, CharField, Func
from django.db.models.functions import Concat
from django.db import connection



from config import models
from config import serializers



class productList(generics.ListCreateAPIView):
    queryset = models.Products.objects.order_by('id')
    serializer_class = serializers.ProductsSerializer
    

class productEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    lookup_url_kwarg = "id"


class companyList(generics.ListCreateAPIView):
    queryset = models.company.objects.order_by('id')
    serializer_class = serializers.companySerializer


class companyEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.company.objects.all()
    serializer_class = serializers.companySerializer
    lookup_url_kwarg = "id"


class plantList(generics.ListCreateAPIView):
    queryset = models.plant.objects.order_by('id')
    serializer_class = serializers.plantSerializer


class plantEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.plant.objects.all()
    serializer_class = serializers.plantSerializer
    lookup_url_kwarg = "id"


class shopfloorList(generics.ListCreateAPIView):
    queryset = models.shopfloor.objects.order_by('id')
    serializer_class = serializers.shopfloorSerializer


class shopfloorEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.shopfloor.objects.all()
    serializer_class = serializers.shopfloorSerializer
    lookup_url_kwarg = "id"


class assemblylineList(generics.ListCreateAPIView):
    queryset = models.assemblyline.objects.order_by('id')
    serializer_class = serializers.assemblylineSerializer


class assemblylineEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.assemblyline.objects.all()
    serializer_class = serializers.assemblylineSerializer
    lookup_url_kwarg = "id"


class machineList(generics.ListCreateAPIView):
    queryset = models.machine.objects.order_by('id')
    serializer_class = serializers.machineSerializer

class machineEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.machine.objects.all()
    serializer_class = serializers.machineSerializer
    lookup_url_kwarg = "id"

class batchList(generics.ListCreateAPIView):
    queryset = models.batch.objects.order_by('id')
    serializer_class = serializers.batchSerializer

class batchEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.batch.objects.all()
    serializer_class = serializers.batchSerializer
    lookup_url_kwarg = "id"

class poNoList(generics.ListCreateAPIView):
    queryset = models.poNo.objects.order_by('id')
    serializer_class = serializers.poNoSerializer

class poNoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.poNo.objects.all()
    serializer_class = serializers.poNoSerializer
    lookup_url_kwarg = "id"

class productReceipeList(generics.ListCreateAPIView):
    queryset = models.ProductRecipe2.objects.order_by('id')
    serializer_class = serializers.productReceipeSerializer

class productReceipeEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductRecipe2.objects.all()
    serializer_class = serializers.productReceipePostSerializer
    lookup_url_kwarg = "id"

class attendanceRulesList(generics.ListCreateAPIView):
    queryset = models.attendanceRules.objects.order_by('id')
    serializer_class = serializers.attendanceRulesSerializer

class attendanceRulesEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.attendanceRules.objects.all()
    serializer_class = serializers.attendanceRulesSerializer
    lookup_url_kwarg = "id"

class departmentList(generics.ListCreateAPIView):
    queryset = models.department.objects.order_by('id')
    serializer_class = serializers.departmentSerializer

class departmentEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.department.objects.all()
    serializer_class = serializers.departmentSerializer
    lookup_url_kwarg = "id"


class designationList(generics.ListCreateAPIView):
    queryset = models.designation.objects.order_by('id')
    serializer_class = serializers.designationSerializer

class designationEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.designation.objects.all()
    serializer_class = serializers.designationSerializer
    lookup_url_kwarg = "id"


class GroupConcat(Func):
    function = 'GROUP_CONCAT'  # Use 'GROUP_CONCAT' for MySQL or 'GroupConcat' for SQLite
    template = "%(function)s(%(expressions)s)"
    separator = ', '


class QcDefectTypeView(generics.ListCreateAPIView):
    queryset = models.QCDefectType.objects.order_by('parameter_id')
    serializer_class = serializers.QCDefectTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parameter_id']




class QcDefectTypeEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QCDefectType.objects.all()
    serializer_class = serializers.QCDefectTypeSerializer
    lookup_url_kwarg = "id"


class InspectionParameterList(generics.ListCreateAPIView):
    queryset = models.InspectionParameters.objects.order_by('id')
    serializer_class = serializers.InspectionParameterSerializer

class InspectionParameterEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InspectionParameters.objects.all()
    serializer_class = serializers.InspectionParameterSerializer
    lookup_url_kwarg = "id"


class CountAPIView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        data = {
            'plant_count': models.plant.objects.count(),
            'shopfloor_count': models.shopfloor.objects.count(),
            'assemblyline_count': models.assemblyline.objects.count(),
            'machine_count': models.machine.objects.count(),
        }
        return Response(data)
    


class ShiftTimingList(generics.ListCreateAPIView):
    queryset = models.ShiftTiming.objects.order_by('id')
    serializer_class = serializers.ShiftTimingSerializer

class ShiftTimingEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ShiftTiming.objects.all()
    serializer_class = serializers.ShiftTimingSerializer
    lookup_url_kwarg = "id"