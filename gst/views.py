from django.shortcuts import render
from django.http import JsonResponse
import json
from core.forms import UploadMultipleFileForm, UploadSingleFileForm
from helper.string_to_list import string_to_list_converter
from django.contrib.auth.decorators import login_required
# from http import HTTPStatus

from utilities.gst_check import process_gst_list
from utilities.gstr1_to_excel import gstr1_to_excel
from utilities.gstr2a_merge import gstr2a_merge
from utilities.gstr2b_merge import gstr2b_merge
from utilities.gstr2b_to_excel import gstr2b_to_excel

# Create your views here.
@login_required()
def gst_number_check(request):
    if request.method == 'POST':
        try:
            number = request.POST.get('gst_numbers')
            if number:
                gst_list = string_to_list_converter(number)
                finalchk = process_gst_list(gst_list)
                print(finalchk)
                return JsonResponse({"success": json.loads(finalchk)}, safe = False, status=200)
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
                # for f in files:
                #     output_file = gstr2a_merge(f)
                #     print(output_file,"outputfile,\n\n\n\n\n\n")
                output_file = gstr2a_merge(files)
                print(output_file,"outputfile,\n\n\n\n\n\n")
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadMultipleFileForm()
        # try:            
        #     form = UploadMultipleFileForm(request.POST, request.FILES)
        #     files = request.FILES.getlist('files')
        #     # if form.is_valid():
        #     for f in files:
        #         print(f,"this------\n\n\n")
        #         # handle_uploaded_file(f)
        #     context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
        #     return render(request, "multiple.html", context)
        #     # else:
        #     #     form = UploadMultipleFileForm()
        # except Exception as e:
        #   return JsonResponse({"error": str(e)}, status=500)  
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
                # for f in files:
                #     output_file = gstr2a_merge(f)
                #     print(output_file,"outputfile,\n\n\n\n\n\n")
                output_file = gstr2b_merge(files)
                print(output_file,"outputfile,\n\n\n\n\n\n")
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
                # for f in files:
                #     output_file = gstr2a_merge(f)
                #     print(output_file,"outputfile,\n\n\n\n\n\n")
                output_file = gstr1_to_excel(files)
                print(output_file,"outputfile,\n\n\n\n\n\n")
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
    if request.method == 'POST':
        try:
            form = UploadSingleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            print(files,"this--\n\n\n\n")
            if form.is_valid():
                # for f in files:
                #     output_file = gstr2a_merge(f)
                #     print(output_file,"outputfile,\n\n\n\n\n\n")
                output_file = gstr2b_to_excel(files)
                print(output_file,"outputfile,\n\n\n\n\n\n")
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
