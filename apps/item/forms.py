from django import forms
from apps.serviceorder.forms import ServiceOrderForm
from apps.subitem.models import SubItem

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
        self.fields['subitem'] = forms.ModelMultipleChoiceField(queryset=SubItem.objects.filter(main_item=None, company=self.company))

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.company = self.company
        instance.save()

    class Meta: 
        model = Item
        fields = ['name', 'description', 'quantity']
