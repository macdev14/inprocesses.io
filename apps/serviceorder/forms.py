from dataclasses import field
from pyexpat import model
from django import forms
from .models import ServiceOrder
from ..subserviceorder.models import SubServiceOrder
from ..forms_addons import CompanyAddonForm

# CompanyAddonForm extends forms.Models

class ServiceOrderForm(CompanyAddonForm):

    
    
    def __init__(self, *args, **kwargs):
        
        self.request = kwargs.pop("request")
        #self.service_order_id = kwargs.pop('service_order_id','')
        self.get_company()
        super(ServiceOrderForm, self).__init__(*args, **kwargs)
        self.fields['subserviceorders'] = forms.ModelMultipleChoiceField(label='Sub ordem de serviços',queryset=SubServiceOrder.objects.filter(main_os=None, company=self.company))
    class Meta: 
        model = ServiceOrder
        fields = ['client']

    def save(self, commit=True):
        instance = super(ServiceOrderForm, self).save(commit=False)
        instance.company = self.company
        instance.save()
        for i in instance.subserviceorders:
            so = SubServiceOrder.objects.get(pk=i.id)
            so.mainos = instance
            so.save()
        


