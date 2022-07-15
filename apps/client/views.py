from multiprocessing.connection import Client
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from apps.client.models import Client
from .forms import ClientForm
from apps.views_addons import CompanyAddonListView, CompanyAddonCreateView, CompanyAddonUpdateView
from django.contrib import messages
# Create your views here.
class ListClient(CompanyAddonListView):

    model = Client
    template_name = 'serviceordercontrol/item/list-item.html'

    def get_queryset(self):
        self.get_company() 
        return Client.objects.filter(company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

    
class CreateClient(CompanyAddonCreateView):
    form_class = ClientForm
    model = Item
    template_name = 'serviceordercontrol/item/add-item.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

class UpdateClient(CompanyAddonUpdateView):
    form_class = ClientForm
    template_name = 'serviceordercontrol/item/update-item.html'
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs