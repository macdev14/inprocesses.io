from django.db import models

from apps.authentication.models import Company
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField, BRStateField
# Create your models here.

class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)
    company_document = BRCNPJField(verbose_name="CNPJ", max_length=512, blank=True)
    
