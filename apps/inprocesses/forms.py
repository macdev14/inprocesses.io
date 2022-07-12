
from django import forms
from .models import ServiceOrderHistory


class ServiceOrderHistoryForm(forms.ModelForm):
    model = ServiceOrderHistory
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        #self.service_order_id = kwargs.pop('service_order_id','')
        super(ServiceOrderHistoryForm, self).__init__(*args, **kwargs)
        #self.fields['serviceorders'] = forms.ModelChoiceField(queryset=ServiceOrder.objects.filter(main_os=self.service_order_id, company=self.company))
    
    class Meta: 
        model = ServiceOrderHistory
        fields = '__all__'