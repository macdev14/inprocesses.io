from unicodedata import name
from django.db import models

from apps.authentication.models import Company

# Create your models here.

class Item(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)
    description = models.CharField(verbose_name="Descrição", max_length=512, blank=True)