from django.db import models
import uuid
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from keel.Core.models import TimeStampedModel, SoftDeleteModel


class Plan(TimeStampedModel, SoftDeleteModel):
    title = models.CharField(max_length=512, null=True, default=None, blank=True)
    description = models.TextField(null=True, blank=True, default=None)
    discount = models.PositiveSmallIntegerField(default=0, blank=True, null=True) # in percentage
    price = models.FloatField(null=True, blank=True, default=True)
    currency = models.CharField(max_length=10, null=True, blank=True, default=None)
    country_iso = models.CharField(max_length=512, null=True, blank=True, default=None)
    sgst = models.PositiveSmallIntegerField(default=0, null=True, blank=True) # in percentage
    cgst = models.PositiveSmallIntegerField(default=0, null=True, blank=True) # in percentage
    is_active = models.BooleanField(default=True)

    def get_plan(self):
        return self
    
    def get_discount_price(self):
        discount = self.discount/100
        discount_price = self.price - (self.price*discount)
        return discount_price

    def get_total_amount(self):
        return self.price

    def get_payment_amount(self):
        return self.price

    def get_currency(self):
        return self.currency

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


class Vendor(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=512, null=True, blank=True, default=None)


class Service(TimeStampedModel, SoftDeleteModel):
    title = models.CharField(max_length=512, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=False)
    fulfillment = models.ForeignKey(Vendor,verbose_name="Vendor", related_name="Vendors", null=True, blank=True, default=None, on_delete=DO_NOTHING)
    price = models.FloatField(null=True, blank=True, default=None)
    currency = models.CharField(max_length=512, null=True, blank=True, default=None) 
    country_iso = models.CharField(max_length=512, null=True, blank=True, default=None)
    plans = models.ManyToManyField(Plan, through = "ServicesPlans", blank = True)

    def get_plan(self):
        return None

    def get_total_amount(self):
        return self.price

    def get_payment_amount(self):
        return self.price

    def get_currency(self):
        return self.currency


class ServicesPlans(TimeStampedModel, SoftDeleteModel):

    plan = models.ForeignKey(Plan, on_delete=models.deletion.DO_NOTHING, related_name='plans_services')
    service = models.ForeignKey(Service, on_delete=models.deletion.DO_NOTHING, related_name='services_plans')
