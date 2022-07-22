from django.shortcuts import render
from django.urls import reverse
from apps.process.models import Process
from .forms import ProcessForm
from apps.views_addons import CompanyAddonListView, CompanyAddonCreateView, CompanyAddonUpdateView
from django.contrib import messages
# Create your views here.
class ListProcess(CompanyAddonListView):
    ordering = ['name']
    paginate_by=10
    model = Process
    template_name = 'serviceordercontrol/processes/list-processes.html'

    def get_queryset(self):
        self.get_company() 
        return Process.objects.filter(company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'processes'
        return super().get_context_data(**kwargs)

    
class CreateProcess(CompanyAddonCreateView):
    form_class = ProcessForm
    model = Process
    template_name = 'serviceordercontrol/processes/create-process.html'

    def get_queryset(self):
        self.get_company() 
        return Process.objects.filter(company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'processes'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
       
        return reverse('process:list')

class UpdateProcess(CompanyAddonUpdateView):
    form_class = ProcessForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
       
        return reverse('process:list')