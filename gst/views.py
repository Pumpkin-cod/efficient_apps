from django.shortcuts import render
from django.http import JsonResponse

from utilities.gst_check import get_gst_check
# from http import HTTPStatus

# Create your views here.

def gst_number_check(request):
    if request.method == 'POST':
        try:
            number = request.POST.get('gst_numbers')
            if number:
                finalchk = get_gst_check(number)
                # print(finalchk,"\n\n\n\n")
                return JsonResponse({"success": finalchk}, status=200)
            else:
                return JsonResponse({"error": "GST number missing"},status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500) 
    return render(request, 'gst/check_number.html')