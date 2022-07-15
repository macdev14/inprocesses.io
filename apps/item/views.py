from django.shortcuts import render
from apps.item.models import Item
from .forms import ItemForm
from apps.views_addons import CompanyAddonListView, CompanyAddonCreateView, CompanyAddonUpdateView
from django.contrib import messages
# Create your views here.


class ListItem(CompanyAddonListView):

    model = Item
    template_name = 'serviceordercontrol/item/list-item.html'

    def get_queryset(self):
        self.get_company() 
        return Item.objects.filter(company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

    
class CreateItem(CompanyAddonCreateView):
    form_class = ItemForm
    model = Item
    template_name = 'serviceordercontrol/item/add-item.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

class UpdateItem(CompanyAddonUpdateView):
    form_class = ItemForm
    template_name = 'serviceordercontrol/item/update-item.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(UpdateItem).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs