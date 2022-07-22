from dataclasses import field
from pyexpat import model
from django import forms

from apps.item.models import Item
from .models import SubItem
from ..subserviceorder.models import SubServiceOrder
from ..forms_addons import CompanyAddonForm

# CompanyAddonForm extends forms.Models

class SubItemForm(CompanyAddonForm):

    
    
    def __init__(self, *args, **kwargs):
        
        self.request = kwargs.pop("request")
        self.item_id = kwargs.pop('item_id','')
        self.get_company()
        super(SubItemForm, self).__init__(*args, **kwargs)
        self.fields['main_item'] = forms.ModelChoiceField( empty_label='Selecione um Item Matriz', label='Item', queryset=Item.objects.filter(company=self.company))
    class Meta: 
        model = SubItem
        fields = ['name', 'description', 'quantity']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.company = self.company
        instance.save()
        # for i in instance.subserviceorders:
        #     so = SubServiceOrder.objects.get(pk=i.id)
        #     so.mainos = instance
        #     so.save()
    


