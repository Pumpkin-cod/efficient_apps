from django.urls import path
from . import views

app_name='gst'
urlpatterns = [
    path('gst_number_check', views.gst_number_check, name='gst_number_check'),
    path('gstr_merge_excel', views.gstr_merge_excel, name='gstr_merge_excel'),
]