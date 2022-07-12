from django import forms
from apps.serviceorder.forms import ServiceOrderForm

from apps.serviceorder.models import ServiceOrder
from apps.subserviceorder.models import SubServiceOrder
from apps.views_addons import CompanyAddonCreateView


class SubServiceOrderForm(CompanyAddonCreateView):
    model = SubServiceOrder
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.service_order_id = kwargs.pop('service_order_id','')
        super(ServiceOrderForm, self).__init__(*args, **kwargs)
        self.fields['serviceorders'] = forms.ModelChoiceField(queryset=ServiceOrder.objects.filter(main_os=self.service_order_id, company=self.company))

    class Meta: 
        model = SubServiceOrder
        fields = '__all__'
