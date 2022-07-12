from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from .serviceorder.forms import *
#from .permissions import EmployeePermission
from apps.authentication.models import *
# Create your views here.



class CompanyAddonListView(ListView):
    
    company = None

    

    def get_company(self):
        if self.request.user.is_employee:
            employee = Employee.objects.get(user=self.request.user)
            self.company = employee.company
        elif self.request.user.is_company:
            company = Company.objects.get(user=self.request.user)
            self.company = company 

class CompanyAddonUpdateView(UpdateView):

    company = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_company(self):
        if self.request.user.is_employee:
            employee = Employee.objects.get(user=self.request.user)
            self.company = employee.company
        elif self.request.user.is_company:
            company = Company.objects.get(user=self.request.user)
            self.company = company 

class CompanyAddonCreateView(CreateView):
    
    company = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_company(self):
        if self.request.user.is_employee:
            employee = Employee.objects.get(user=self.request.user)
            self.company = employee.company
        elif self.request.user.is_company:
            company = Company.objects.get(user=self.request.user)
            self.company = company 

