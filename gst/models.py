# import os
from django.db import models

from core.models import User
from core.validators import ExcelFileValidator
# Create your models here.



class Gstr2aMergeExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Gstr2aFiles(models.Model):
    gstr_2a_merge_excel = models.ForeignKey(Gstr2aMergeExcel, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Gstr2aMergeExcel/", validators=[ExcelFileValidator()])