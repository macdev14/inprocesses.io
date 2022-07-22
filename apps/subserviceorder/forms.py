from django import forms
from apps.item.models import Item
from apps.serviceorder.forms import ServiceOrderForm

from apps.serviceorder.models import ServiceOrder
from apps.subserviceorder.models import SubServiceOrder
from apps.forms_addons import CompanyAddonForm


class SubServiceOrderForm(CompanyAddonForm):
    model = SubServiceOrder
    
    #main_os = forms.ModelChoiceField( empty_label='Selecione uma Ordem de Serviço Matriz', label='Ordem de Serviços', queryset=ServiceOrder.objects.filter(company=self.company))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.service_order_id = kwargs.pop('service_order_id','')
        self.get_company()
        # print('company: ', self.company.id)
        
        super(SubServiceOrderForm, self).__init__(*args, **kwargs)
        print(self.fields)
        self.fields['main_os'] = forms.ModelChoiceField( empty_label='Selecione uma Ordem de Serviço Matriz', label='Ordem de Serviços', queryset=ServiceOrder.objects.filter(company=self.company))
        self.fields['subitem'] = forms.ModelChoiceField( empty_label='Selecione um Item', label='Item', queryset=Item.objects.filter(company=self.company))
    class Meta: 
        model = SubServiceOrder
        fields = ['main_os', 'subitem', 'quantity']
