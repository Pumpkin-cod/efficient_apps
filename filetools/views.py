import os
from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from pathlib import Path

# ---Local Imports---
from core.forms import UploadMultipleFileForm
from filetools.models import CombineExcel, CombineExcelFiles
from filetools.utilities.combine_excel import combine_excel

# Create your views here.

def combine_excel_files(request):
    form = ""
    if request.method == 'POST':
        try:
            form = UploadMultipleFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            if form.is_valid():
                if len(files) <= 1:
                    return JsonResponse({"error": "Invalid Input! Please select more than one file to merge"}, status=400)
                _combine_excel = CombineExcel.objects.all()
                _combine_excel_files = CombineExcelFiles.objects.all()
                file_list = []

                for f in files:
                    inst_combine_excel = _combine_excel.create(user = request.user)
                    file = _combine_excel_files.create(combine_excel = inst_combine_excel, file = f)
                    file_list.append(file)

                file_path_list = []
                BASE_DIR = Path(__file__).resolve().parent.parent
                for i in file_list:
                    file_path_list.append(os.path.join(BASE_DIR, "upload", str(i.file)))
                print(file_path_list,"----Link----")
                output_file = combine_excel(file_path_list)
                print(output_file,"Combine Output\n\n\n\n\n")
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
                print(response,"Response-----\n\n\n\n")
                return response
                # return JsonResponse({"success": "Files Merged Successfully"}, status=200)
            else:
                return JsonResponse({"error":"Invalid Form"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadMultipleFileForm() 
    return render(request, 'filetools/combine_excel.html', {'form': form})
