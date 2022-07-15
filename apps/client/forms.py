from multiprocessing.connection import Client
from django import forms
from apps.serviceorder.forms import ServiceOrderForm

from .models import Client
#from apps.item.models import SubServiceOrder
from apps.forms_addons import CompanyAddonForm


class ClientForm(CompanyAddonForm):
    model = Client
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.service_order_id = kwargs.pop('service_order_id','')
        super(ClientForm, self).__init__(*args, **kwargs)
        # self.fields['serviceorders'] = forms.ModelChoiceField(queryset=ServiceOrder.objects.filter(main_os=self.service_order_id, company=self.company))

    class Meta: 
        model = Client
        fields = ['name', 'company_document']
