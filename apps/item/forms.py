from django import forms
from apps.serviceorder.forms import ServiceOrderForm

from .models import Item
#from apps.item.models import SubServiceOrder
from apps.forms_addons import CompanyAddonForm


class ItemForm(CompanyAddonForm):
    model = Item
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.service_order_id = kwargs.pop('service_order_id','')
        self.get_company()
        super(ItemForm, self).__init__(*args, **kwargs)
        # self.fields['serviceorders'] = forms.ModelChoiceField(queryset=ServiceOrder.objects.filter(main_os=self.service_order_id, company=self.company))

    class Meta: 
        model = Item
        fields = ['name', 'description']
