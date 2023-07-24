from django.db import models


class BaseDuty(models.Model):
    class Meta:
        verbose_name = "职责"
        abstract = True
