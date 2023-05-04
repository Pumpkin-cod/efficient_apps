from django.shortcuts import render
from django.http import JsonResponse
import json
from helper.string_to_list import string_to_list_converter
# from http import HTTPStatus

from utilities.gst_check import process_gst_list

# Create your views here.

def gst_number_check(request):
    if request.method == 'POST':
        try:
            number = request.POST.get('gst_numbers')
            if number:
                gst_list = string_to_list_converter(number)
                finalchk = process_gst_list(gst_list)
                print(finalchk,"\n\n\n\n\n")
                return JsonResponse({"success": json.loads(finalchk)}, safe = False, status=200)
            else:
                return JsonResponse({"error": "GST number missing"},status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500) 
    return render(request, 'gst/check_number.html')