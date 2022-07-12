from django.db import models
from django.urls import reverse
from ..authentication.models import Employee
from ..process.models import Process
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
from ..subserviceorder.models import SubServiceOrder
from django.core.mail import send_mail
import datetime as datetime2
from django.utils.translation import gettext_lazy as _
# Create your models here.
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
        
        