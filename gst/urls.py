from django.urls import path
from . import views

app_name='gst'
urlpatterns = [
    path('gst_number_check', views.gst_number_check, name='gst_number_check'),
    path('gstr_2a_merge_excel', views.gstr_2a_merge_excel, name='gstr_2a_merge_excel'),
    path('gstr_2b_merge_excel', views.gstr_2b_merge_excel, name='gstr_2b_merge_excel'),
    path('gstr_1_json_to_excel', views.gstr_1_json_to_excel, name='gstr_1_json_to_excel'),
    path('gstr_2B_json_to_excel', views.gstr_2B_json_to_excel, name='gstr_2B_json_to_excel'),
    path('gstr_3B_pdf_to_excel', views.gstr_3B_pdf_to_excel, name='gstr_3B_pdf_to_excel'),
]