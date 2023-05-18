from django.urls import path

# ---Local Imports---
from . import views

app_name='file_tools'
urlpatterns = [
    # ---Excel Tools---
    path('combine_excel', views.combine_excel_files, name='combine_excel'),
    # path('split_excel', views.split_excel, name='split_excel'),

    # ---Pdf Tools---
    # path('split_pdf', views.split_pdf, name='split_pdf'),
    # path('sort_pdf', views.sort_pdf, name='sort_pdf'),
    # path('add_number_to_pdf', views.add_number_to_pdf, name='add_number_to_pdf'),
    # path('encrypt_pdf', views.encrypt_pdf, name='encrypt_pdf'),
    # path('decrypt_pdf', views.decrypt_pdf, name='decrypt_pdf'),
    # path('delete_pages', views.sort_pdf, name='delete_pages'),
    # path('rotate_pdf', views.sort_pdf, name='rotate_pdf'),

    # ---Other Tools---
    # path('combine_text_files', views.combine_text_files, name='combine_text_files'),
    # path('excel_to_pdf', views.excel_to_pdf, name='excel_to_pdf'),
    # path('ppt_to_pdf', views.ppt_to_pdf, name='ppt_to_pdf'),
    # path('word_to_pdf', views.word_to_pdf, name='word_to_pdf'),
]