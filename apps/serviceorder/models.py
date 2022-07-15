# -*- encoding: utf-8 -*-

from django.db import models
from django.urls import reverse
from apps.authentication.models import *
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField, BRStateField
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
import datetime as datetime2
from django.core.mail import send_mail

from apps.client.models import Client

from apps.process.models import Process


class ServiceOrder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    #sub_os = models.ManyToOneRel(to=SubServiceOrder,on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    number =  models.IntegerField(default=1)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_number = self.objects.all().aggregate(largest=models.Max('number'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_number is not None:
                self.number = last_number + 1

        super(ServiceOrder, self).save(*args, **kwargs)




