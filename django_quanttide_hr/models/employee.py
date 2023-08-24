"""
员工数据模型
"""

from django_quanttide import models as quanttide_models


class BaseEmployee(quanttide_models.Model):
    org_user_id = quanttide_models.IDField(primary_key=False, verbose_name='组织用户ID')
    created_at = quanttide_models.CreatedAtField()
    updated_at = quanttide_models.UpdatedAtField()

    class Meta:
        abstract = True
        verbose_name = '员工'
        verbose_name_plural = '员工组列表'
