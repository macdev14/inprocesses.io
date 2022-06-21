

# Create your models here.





# from asyncio.streams import _ClientConnectedCallback
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
import datetime as datetime2
from django.core.mail import send_mail

class User(AbstractUser):
    is_employee = models.BooleanField('employee status', help_text='Designates whether the user can log in as an employee.', default=False)
    is_company = models.BooleanField('company status', help_text='Designates whether the user can log in as a company.' , default=False)

# Create your models here.

    
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # email = models.EmailField(_('Endereço de E-mail'), unique=True)
    cnpj = BRCNPJField(_('CNPJ'), unique=True)
    name = models.CharField(verbose_name="Nome da empresa", max_length=512,unique=True, blank=True)
    
    # class Meta:
    #     permissions = [
    #         (

    #         )
    #     ]

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = BRCPFField(_('CPF'), unique=True) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

