from django.urls import re_path
from config import views


urlpatterns = [

    re_path(r'^product/$', views.productList.as_view()),
    re_path(r'^product/(?P<id>\d+)/$', views.productEdit.as_view()),

    re_path(r'^company/$', views.companyList.as_view()),
    re_path(r'^company/(?P<id>\d+)/$', views.companyEdit.as_view()),

    re_path(r'^plant/$', views.plantList.as_view()),
    re_path(r'^plant/(?P<id>\d+)/$', views.plantEdit.as_view()),

    re_path(r'^shopfloor/$', views.shopfloorList.as_view()),
    re_path(r'^shopfloor/(?P<id>\d+)/$', views.shopfloorEdit.as_view()),

    re_path(r'^assemblyline/$', views.assemblylineList.as_view()),
    re_path(r'^assemblyline/(?P<id>\d+)/$', views.assemblylineEdit.as_view()),

    re_path(r'^machine/$', views.machineList.as_view()),
    re_path(r'^machine/(?P<id>\d+)/$', views.machineEdit.as_view()),

    re_path(r'^batch/$', views.batchList.as_view()),
    re_path(r'^batch/(?P<id>\d+)/$', views.batchEdit.as_view()),

    re_path(r'^poNo/$', views.poNoList.as_view()),
    re_path(r'^poNo/(?P<id>\d+)/$', views.poNoEdit.as_view()),

    re_path(r'^productReceipe/$', views.productReceipeList.as_view()),
    re_path(r'^productReceipe/(?P<id>\d+)/$', views.productReceipeEdit.as_view()),

    re_path(r'^attendanceRules/$', views.attendanceRulesList.as_view()),
    re_path(r'^attendanceRules/(?P<id>\d+)/$', views.attendanceRulesEdit.as_view()),

    re_path(r'^department/$', views.departmentList.as_view()),
    re_path(r'^department/(?P<id>\d+)/$', views.departmentEdit.as_view()),

    re_path(r'^designation/$', views.designationList.as_view()),
    re_path(r'^designation/(?P<id>\d+)/$', views.designationEdit.as_view()),

    re_path(r'^qc_defect_type/$', views.QcDefectTypeView.as_view()),
    re_path(r'^qc_defect_type/(?P<id>\d+)/$', views.QcDefectTypeEdit.as_view()),

    re_path(r'^inspection_parameter/$', views.InspectionParameterList.as_view()),
    re_path(r'^inspection_parameter/(?P<id>\d+)/$', views.InspectionParameterEdit.as_view()),

    re_path(r'^shift/$', views.ShiftTimingList.as_view()),
    re_path(r'^shift/(?P<id>\d+)/$', views.ShiftTimingEdit.as_view()),

    re_path(r'^dash_card_count/$', views.CountAPIView.as_view()),

]