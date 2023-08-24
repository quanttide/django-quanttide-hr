"""
员工组数据模型
"""

from django_quanttide import models as quanttide_models


class BaseEmployeeGroup(quanttide_models.PolymorphicModel):
    org_user_group_id = quanttide_models.IDField(primary_key=False, verbose_name='组织用户组ID')
    created_at = quanttide_models.CreatedAtField()
    updated_at = quanttide_models.UpdatedAtField()
    name = quanttide_models.NameField()
    verbose_name = quanttide_models.VerboseNameField()

    class Meta:
        verbose_name = '员工组'
        verbose_name_plural = '员工组列表'
        abstract = True


class BaseDepartment(BaseEmployeeGroup):
    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门列表'
        abstract = True


class BaseCommittee(BaseEmployeeGroup):
    class Meta:
        verbose_name = '委员会'
        verbose_name_plural = '委员会列表'
        abstract = True
