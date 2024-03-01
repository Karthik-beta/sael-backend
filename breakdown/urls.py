from django.urls import re_path, path
from . import views

from .views import (BreakdownCategoryListCreateView,
                       BreakdownCategoryRetrieveUpdateDestroyView,
                       DownloadAndonData,
                       AndonDataListCreateView, DownloadBreakdownHMIData, AndonMetricsView, Shopfloorwise,
                       check_database_connection, AndonDataOpenListView,
                       AndonDataOpenResettingListView, AndonDataOpenEngineeringListView, AndonDataOpenElectListView, AndonDataOpenQualityListView, AndonDataOpenMechListView)


urlpatterns = [

    re_path(r'^breakdown_category/$', BreakdownCategoryListCreateView.as_view()),
    re_path(r'^breakdown_category/(?P<breakdownCategoryId>\d+)/?$', BreakdownCategoryRetrieveUpdateDestroyView.as_view()),

    # re_path(r'^shift/$', ShiftListCreateView.as_view()),

    # re_path(r'^company/$', CompanyListCreateView.as_view()),

    # re_path(r'^location/$', LocationListCreateView.as_view()),

    # re_path(r'^shopfloor/$', ShopfloorListCreateView.as_view()),

    # re_path(r'^assemblyline/$', AssemblylineListCreateView.as_view()),

    # re_path(r'^machine/$', MachineListCreateView.as_view()),

    # re_path(r'^andon/$', views.andonapi),  
    re_path(r'^andon/([0-9]+)$', views.andonapi),

    re_path(r'^andon/$', AndonDataListCreateView.as_view()),

    # re_path(r'^export_andon/$', DownloadAndonData.as_view(), name='export_xlsx'),

    re_path(r'^export_hmi/$', DownloadBreakdownHMIData.as_view(), name='export_hmi_xlsx'),

    re_path(r'^export/$', DownloadAndonData.as_view(), name='export_xlsx'),

    re_path(r'^metrics/$', AndonMetricsView.as_view()),

    re_path(r'^shopfloorwise/$', Shopfloorwise.as_view()),

    re_path(r'^check_database_connection/$', check_database_connection),

    re_path(r'^andon_open/$', AndonDataOpenListView.as_view()),

    re_path(r'^andon_open_resetting/$', AndonDataOpenResettingListView.as_view()),

    re_path(r'^andon_open_engineering/$', AndonDataOpenEngineeringListView.as_view()),

    re_path(r'^andon_open_elect/$', AndonDataOpenElectListView.as_view()),

    re_path(r'^andon_open_quality/$', AndonDataOpenQualityListView.as_view()),

    re_path(r'^andon_open_mech/$', AndonDataOpenMechListView.as_view()),

    # path('register', RegisterView.as_view()),
    # path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    # path('logout', LogoutView.as_view()),

]