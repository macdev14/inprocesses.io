from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import SubItemForm
#from .permissions import EmployeePermission
from apps.serviceorder.models import *
# Create your views here.
from apps.views_addons import CompanyAddonListView, CompanyAddonUpdateView, CompanyAddonCreateView




class CreateSubItem(CompanyAddonCreateView):
    form_class = SubItemForm
    template_name = 'serviceordercontrol/subitem/add-subitem.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'SubItem'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class UpdateSubItem(CompanyAddonUpdateView):
    form_class = SubItemForm
    template_name = 'serviceordercontrol/subitem/update-subitem.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'SubItem'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
class ListSubItem(CompanyAddonListView):
    paginate_by = 10
    ordering = ['name']
    model = ServiceOrder
    template_name = 'serviceordercontrol/subitem/list-subitem.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'SubItem'
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.get_company() 
        return ServiceOrder.objects.filter(company=self.company)
