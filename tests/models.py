from django.db import models
from django_quanttide_hr.models import BaseEmployee, BaseEmployeeGroup


class Employee(BaseEmployee):
    real_name = models.CharField(max_length=255, verbose_name='真实姓名')


class EmployeeGroup(BaseEmployeeGroup):
    employees = models.ManyToManyField(Employee, verbose_name='员工')
