from django.db import models

from apps.authentication.models import Company

# Create your models here.
class Process(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)
