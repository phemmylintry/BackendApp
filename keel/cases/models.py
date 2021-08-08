import uuid
from django.db import models

from keel.Core.models import TimeStampedModel, SoftDeleteModel
from keel.plans.models import Plan
from keel.authentication.models import User

from .constants import SORT_COLUMN_MAP

class CaseManager(models.Manager):

    def get_agent_cases(self, agent, req_dict):

        sort_column = req_dict.get("sort_column")
        sort_order = req_dict.get("sort_order")

        sort_list = ["-updated_at"] # default sort
        if sort_column:
            colmn_value = SORT_COLUMN_MAP.get(sort_column, "")
            if colmn_value and sort_order:
                sort_order_value = "" if sort_order == "asc" else "-"
                sort_list = [sort_order_value + colmn_value]

        queryset = self.filter(agent = agent).order_by(*sort_list)

        return queryset

class Case(TimeStampedModel, SoftDeleteModel):

    BOOKED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4

    CASES_TYPE_CHOICES = (
        (BOOKED, 'BOOKED'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (COMPLETED, 'COMPLETED'),
        (CANCELLED, 'CANCELLED'),
    )

    case_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name='users_cases')
    agent = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name='agents_cases')
    account_manager_id = models.IntegerField(null=True, blank=True, default=None)
    status = models.PositiveSmallIntegerField(choices=CASES_TYPE_CHOICES, verbose_name="case_status", default=BOOKED)
    is_active = models.BooleanField(verbose_name= 'Active', default=True)
    ref_id = models.ForeignKey('self',null=True, blank=True, on_delete=models.deletion.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete=models.deletion.DO_NOTHING, related_name='plans_cases')

    def save(self, *args, **kwargs):
        self.case_id = uuid.uuid4()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.case_id)

    objects = CaseManager()