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


class Gstr2bMergeExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Gstr2bFiles(models.Model):
    gstr_2b_merge_excel = models.ForeignKey(Gstr2bMergeExcel, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Gstr2bMergeExcel/", validators=[ExcelFileValidator()])


class Gstr1JsonToExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="Gstr1JsonToExcel/")


class Gstr2bJsonToExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="Gstr2bJsonToExcel/")
