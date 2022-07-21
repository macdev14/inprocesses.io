
from django import forms
from .models import Process
from ..forms_addons import CompanyAddonForm

class ProcessForm(CompanyAddonForm):
    model = Process
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.get_company()
        #self.service_order_id = kwargs.pop('service_order_id','')
        super(ProcessForm, self).__init__(*args, **kwargs)
        #self.fields['serviceorders'] = forms.ModelChoiceField(queryset=ServiceOrder.objects.filter(main_os=self.service_order_id, company=self.company))
    
    class Meta: 
        model = Process
        fields = ['name']