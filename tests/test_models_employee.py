from django.test import TestCase

from tests.models import Employee


class BaseEmployeeTestCase(TestCase):
    def test_default(self):
        employee = Employee.objects.create()


