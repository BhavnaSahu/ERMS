from django.contrib import admin

# Register your models here.
from employee.models import EmployeeDetail, EmployeeEducation, EmployeeExperience

admin.site.register(EmployeeDetail)
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)