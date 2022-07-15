from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import *
#from .permissions import EmployeePermission
from apps.serviceorder.models import *
# Create your views here.
from apps.views_addons import CompanyAddonListView, CompanyAddonUpdateView, CompanyAddonCreateView




class CreateServiceOrder(CompanyAddonCreateView):
    form_class = ServiceOrderForm
    template_name = 'serviceordercontrol/serviceorders/add-serviceorders.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'serviceorder'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class UpdateServiceOrder(CompanyAddonUpdateView):
    form_class = ServiceOrderForm
    template_name = 'serviceordercontrol/serviceorders/update-serviceorders.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'serviceorder'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
class ListServiceOrders(CompanyAddonListView):

    model = ServiceOrder
    template_name = 'serviceordercontrol/serviceorders/list-serviceorders.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'serviceorder'
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.get_company() 
        return ServiceOrder.objects.filter(company=self.company)
