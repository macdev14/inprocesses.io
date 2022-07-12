from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ServiceOrderHistory
from .forms import ServiceOrderHistoryForm
from apps.views_addons import CompanyAddonListView, CompanyAddonCreateView, CompanyAddonUpdateView

# Create your views here.
class ListServiceOrderHistory(CompanyAddonListView):

    model = ServiceOrderHistory
    template_name = 'serviceordercontrol/inprocesses/list-inprocesses.html'

    def get_queryset(self):
        self.get_company() 
        return ServiceOrderHistory.objects.filter(employee__company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'service-order-history'
        return super().get_context_data(**kwargs)

class CreateServiceOrderHistory(CompanyAddonCreateView):
    form_class = ServiceOrderHistoryForm
    model = ServiceOrderHistory
    template_name = 'serviceordercontrol/inprocesses/create-inprocesses.html'

    def get_queryset(self):
        self.get_company() 
        return ServiceOrderHistory.objects.filter(employee__company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'service-order-history'
        return super().get_context_data(**kwargs)

class UpdateServiceOrderHistory(CompanyAddonUpdateView):
    form_class = ServiceOrderHistoryForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs