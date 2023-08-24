from django.db import models


class BaseDuty(models.Model):
    class Meta:
        verbose_name = "职责"
        verbose_name_plural = "职责列表"
        abstract = True
