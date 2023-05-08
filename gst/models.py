# import os
from django.db import models

from core.models import User
from core.validators import ExcelFileValidator
# Create your models here.



class Gstr2aMergeExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


# def get_upload_to(instance, file_obj=None):
#     # return 'upload/Gstr2aMergeExcel/%d/%s' % (instance, date)
#     path = ""
#     if file_obj[3] == "gstr_2a_merge_excel":
#         # path = f"{file_obj[2]}/{file_obj[0]}"
#         print(path,"check\n\n\n\n\n")
#     # path = f'{instance}/{date}'
#     return os.path.join("Gstr2aMergeExcel/",file_obj[2],file_obj[0])

class Gstr2aFiles(models.Model):
    gstr_2a_merge_excel = models.ForeignKey(Gstr2aMergeExcel, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Gstr2aMergeExcel/", validators=[ExcelFileValidator()])