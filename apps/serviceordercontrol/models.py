#from django.db import models

# Create your models here.



# Create your models here.

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

class ServiceOrder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    #sub_os = models.ManyToOneRel(to=SubServiceOrder,on_delete=models.DO_NOTHING)
    number =  models.IntegerField()

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


class Client(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)
    company_id = BRCNPJField(verbose_name="CNPJ", max_length=512, blank=True)
    

class SubServiceOrder(models.Model):
    main_os = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    number = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    def save(self, *args, **kwargs):
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_number = self.objects.all().aggregate(largest=models.Max('number'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_number is not None:
                self.number = last_number + 1
        super(SubServiceOrder, self).save(*args, **kwargs)

class Process(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)


class ServiceOrderHistory(models.Model):
    
    
    process = models.ForeignKey(Process, null=True, verbose_name=_("Processo"), on_delete=models.SET_NULL,  related_name="idProcess")
    os = models.ForeignKey(SubServiceOrder, null=True, verbose_name=_("Ordem de Serviço"), on_delete=models.SET_NULL, related_name="idServiceOrder")
    employee = models.ForeignKey(Employee, null=True, verbose_name=_("Colaborador"), on_delete=models.SET_NULL, related_name="idEmployee")
    start = models.TimeField(_("Início"), auto_now_add=True)
    end =  models.TimeField(_("Fim"), null=True, blank=True,auto_now=False, auto_now_add=False)
    incidents = models.TextField(_("Ocorrências"),null=True, blank=True)
    period = models.IntegerField(_("Periodo de tempo"),null=True,blank=True, default=1)
    date = models.DateTimeField( default=now, null=True, blank=True)
    qtd = models.IntegerField(null=True, blank=True, default=1)
    history = HistoricalRecords()
    def __str__(self):
        
        return f"O.S: {self.os.Numero_Os} - {self.processo} - {self.qtd}"
    
    class Meta:
        #db_table = 'Historico_os'
        ordering = ['-end']
        verbose_name = _("Localização O.S")
        verbose_name_plural = _("Localizar O.S")

    def time(self):
        try:
            enter_delta = datetime2.timedelta(hours=self.inicio.hour, minutes=self.inicio.minute, seconds=self.inicio.second)
            exit_delta = datetime2.timedelta(hours=self.fim.hour, minutes=self.fim.minute, seconds=self.fim.second)
            difference_delta = exit_delta - enter_delta
            return difference_delta
        except:
            return 'Não Finalizado'
    def avg_qtd(self):
        try:
            result_hour, plural_hour= None, None
            result =  self.time().total_seconds()/self.qtd/60
            plural = 'minutos' if round(result, 2) > 1 else 'minuto'
            if round(result, 2) >= 60:
                result_hour = round(round(result, 2)/60,2) 
                plural_hour = 'hora(s)'
                plural = plural+' / '
            return f'{round(result, 2)} {plural} {result_hour or ""} {plural_hour or ""}'
        except Exception as e:
            print(e)
            return 'Não Finalizado'
    def date_obj(self):
        try:
            return f'{self.data.day}/{self.data.month}/{self.data.year}'
        except:
            return 'Data não encontrada.'

   
    
    def save(self, *args, **kwargs):
        try:
            lperiod = ServiceOrderHistory.objects.values('period').filter(os=self.os).latest('period')
            lperiod = lperiod['period'] + 1
        except:
            lperiod = 1
        
        self.periodo = lperiod
        super().save(*args, **kwargs)
        domain = 'https://admin.peppertools.com.br'
        info = (self._meta.app_label, self._meta.model_name)
        info_os = (self.os._meta.app_label, self.os._meta.model_name)
        os_url = '\nVeja a Ordem de Serviço em '+ domain + reverse('admin:%s_%s_change' % info_os, args=(self.os.pk,))  
        admin_url = '\nVeja em '+ domain + reverse('admin:%s_%s_change' % info, args=(self.pk,))  
        SubServiceOrder.objects.filter(pk=self.os.id).update(STATUS=self.processo.procname)
        tempo_por_peca = '\nTempo por peça '+str(self.avg_qtd()) if self.fim else ''
        print(tempo_por_peca) 
        tempo = 'iniciada' if not self.fim else 'finalizada'
        subject = 'Ordem de Serviço N. '+ str(self.os.Numero_Os) +' '+tempo+' por '+ self.colaborador.username +' em '+self.processo.procname       
        message = 'Ordem de Serviço '+tempo+' por '+ self.colaborador.username +' em '+self.processo.procname+tempo_por_peca +' '+ admin_url + os_url
        from_email = 'contato@peppertools.com.br'
        send_mail(subject, message, from_email, ['contato@peppertools.com.br'], fail_silently=False)
        
        