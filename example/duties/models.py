from django.db import models
from django_dag.models import node_factory, edge_factory


class Duty(node_factory('DutyUpstreamDownstreamRelation')):
    class Meta:
        verbose_name = "职责"


class DutyUpstreamDownstreamRelation(edge_factory('Duty', concrete=False)):
    class Meta:
        verbose_name = "职责上下游关系"
