import os
from django.shortcuts import render
from django.http import JsonResponse
from django.http import FileResponse
from datetime import datetime
import json
from core.forms import UploadMultipleFileForm, UploadSingleFileForm
from helper.string_to_list import string_to_list_converter
from django.contrib.auth.decorators import login_required
from pathlib import Path

# from http import HTTPStatus

from utilities.gst_check import process_gst_list
from utilities.gstr1_to_excel import gstr1_to_excel
from utilities.gstr2a_merge import gstr2a_merge
from utilities.gstr2b_merge import gstr2b_merge
from utilities.gstr2b_to_excel import gstr2b_to_excel
from gst.models import Gstr1JsonToExcel, Gstr2aFiles, Gstr2aMergeExcel, Gstr2bFiles, Gstr2bJsonToExcel, Gstr2bMergeExcel #get_upload_to
# Create your views here.
@login_required()
def gst_number_check(request):
    if request.method == 'POST':
        try:
            number = request.POST.get('gst_numbers')
            if number:
                gst_list = string_to_list_converter(number)
                finalchk = process_gst_list(gst_list)
                output = finalchk.to_dict()
                return JsonResponse({"success": output}, safe = False, status=200)
            else:
                return JsonResponse({"error": "GST number missing"},status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500) 
    return render(request, 'gst/check_number.html')


@login_required()
def gstr_2a_merge_excel(request):
    form = ""
    if request.method == 'POST':
        try:
            form = UploadMultipleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            if form.is_valid():
                if len(files) <= 1:
                    return JsonResponse({"error": "Invalid Input! Please select more than one file to merge"}, status=400)
                gstr_2a_merge_excel = Gstr2aMergeExcel.objects.all()
                gstr_2a_files = Gstr2aFiles.objects.all()
                file_list = []
                for f in files:
                    inst_gstr_2a_merge_excel = gstr_2a_merge_excel.create(user = request.user)
                    file = gstr_2a_files.create(gstr_2a_merge_excel = inst_gstr_2a_merge_excel, file = f)
                    file_list.append(file)

                file_path_list = []
                BASE_DIR = Path(__file__).resolve().parent.parent
                for i in file_list:
                    file_path_list.append(os.path.join(BASE_DIR, "upload", str(i.file)))
                print(file_path_list[0],"----Link----")
                output_file = gstr2a_merge(file_path_list)
                print(output_file,"Merge Output\n\n\n\n\n")
                working_file_path = output_file.get('all_combined')

                merged_file_path = os.path.abspath(working_file_path)
                merged_file_name = os.path.basename(merged_file_path)

                # Open the merged file and create a FileResponse
                merged_file = open(merged_file_path, 'rb')
                response = FileResponse(merged_file)

                # Set the content type and Content-Disposition header
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment; filename="%s"' % merged_file_name

                # Reset the file pointer to the beginning of the file
                merged_file.seek(0)

                return response
                # return JsonResponse({"success": "Files Merged Successfully"}, status=200)
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadMultipleFileForm()  
    return render(request,'gst/gstr_2a_merge_excel.html', {'form': form})


@login_required()
def gstr_2b_merge_excel(request):
    form = ""
    if request.method == 'POST':
        try:
            form = UploadMultipleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            print(files,"this--\n\n\n\n")
            if form.is_valid():
                if len(files) <= 1:
                    return JsonResponse({"error": "Invalid Input! Please select more than one file to merge"}, status=400)
                gstr_2b_merge_excel = Gstr2bMergeExcel.objects.all()
                gstr_2b_files = Gstr2bFiles.objects.all()
                file_list = []
                for f in files:
                    inst_gstr_2b_merge_excel = gstr_2b_merge_excel.create(user = request.user)
                    file = gstr_2b_files.create(gstr_2b_merge_excel = inst_gstr_2b_merge_excel, file = f)
                    file_list.append(file)
                # output_file = gstr2b_merge(files)
                # print(output_file,"outputfile,\n\n\n\n\n\n")
                file_path_list = []
                BASE_DIR = Path(__file__).resolve().parent.parent
                for i in file_list:
                    file_path_list.append(os.path.join(BASE_DIR, "upload", str(i.file)))
                print(file_path_list[0],"----Link----")
                output_file = gstr2b_merge(file_path_list)
                print(output_file,"Merge Output\n\n\n\n\n")
                working_file_path = output_file.get('all_combined')

                merged_file_path = os.path.abspath(working_file_path)
                merged_file_name = os.path.basename(merged_file_path)

                # Open the merged file and create a FileResponse
                merged_file = open(merged_file_path, 'rb')
                response = FileResponse(merged_file)

                # Set the content type and Content-Disposition header
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment; filename="%s"' % merged_file_name

                # Reset the file pointer to the beginning of the file
                merged_file.seek(0)

                return response
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadMultipleFileForm() 
    return render(request,'gst/gstr_2b_merge_excel.html', {'form': form})


@login_required()
def gstr_1_json_to_excel(request):
    form = ""
    if request.method == 'POST':
        try:
            form = UploadSingleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            print(files,"this--\n\n\n\n")
            if form.is_valid():
                gstr_1_json_to_excel = Gstr1JsonToExcel.objects.create(user=request.user,file=files[0])
                BASE_DIR = Path(__file__).resolve().parent.parent
                file_path = os.path.join(BASE_DIR, "upload", str(gstr_1_json_to_excel.file))
                print(file_path,"file_path\n\n\n\n\n")
                output_file = gstr1_to_excel(file_path)
                print(output_file,"Merge Output\n\n\n\n\n")
                working_file_path = output_file.get('all_combined')

                merged_file_path = os.path.abspath(working_file_path)
                merged_file_name = os.path.basename(merged_file_path)

                # Open the merged file and create a FileResponse
                merged_file = open(merged_file_path, 'rb')
                response = FileResponse(merged_file)

                # Set the content type and Content-Disposition header
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment; filename="%s"' % merged_file_name

                # Reset the file pointer to the beginning of the file
                merged_file.seek(0)

                return response
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadSingleFileForm() 
    return render(request,'gst/gstr_1_json_to_excel.html', {'form': form})


@login_required()
def gstr_2B_json_to_excel(request):
    form = ""
    form = ""
    if request.method == 'POST':
        try:
            form = UploadSingleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            print(files,"this--\n\n\n\n")
            if form.is_valid():
                gstr_2b_json_to_excel = Gstr2bJsonToExcel.objects.create(user=request.user,file=files[0])
                BASE_DIR = Path(__file__).resolve().parent.parent
                file_path = os.path.join(BASE_DIR, "upload", str(gstr_2b_json_to_excel.file))
                print(file_path,"file_path\n\n\n\n\n")
                output_file = gstr2b_to_excel(file_path)
                print(output_file,"Merge Output\n\n\n\n\n")
                working_file_path = output_file.get('all_combined')

                merged_file_path = os.path.abspath(working_file_path)
                merged_file_name = os.path.basename(merged_file_path)

                # Open the merged file and create a FileResponse
                merged_file = open(merged_file_path, 'rb')
                response = FileResponse(merged_file)

                # Set the content type and Content-Disposition header
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment; filename="%s"' % merged_file_name

                # Reset the file pointer to the beginning of the file
                merged_file.seek(0)

                return response
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadSingleFileForm()  
    return render(request,'gst/gstr_2B_json_to_excel.html', {'form': form})


@login_required()
def gstr_3B_pdf_to_excel(request):
    return render(request, 'gst/gstr_3B_pdf_to_excel.html')
