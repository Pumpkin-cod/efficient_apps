from django.db import models

# ---Local Imports---
from core.models import User
from core.validators import ExcelFileValidator


class CombineExcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class CombineExcelFiles(models.Model):
    combine_excel = models.ForeignKey(CombineExcel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='CombineExcel/' ,validators=[ExcelFileValidator()])