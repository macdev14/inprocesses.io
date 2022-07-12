from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView

from apps.authentication.permissions import CreateCompanyPermission
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .permissions import EmployeePermission, NotEmployeePermission
from apps.serviceorder.models import *
from ..views_addons import CompanyAddonListView

# Create your views here.

class EmployeeDashboard(CreateView, EmployeePermission):
    model = ServiceOrder
    template_name = 'employees/employee-dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'employee-dashboard'
        return super().get_context_data(**kwargs)


class ListEmployees(ListView, LoginRequiredMixin, UserPassesTestMixin ):
    model = Employee
    template_name = 'employees/list-employees.html'
    paginate_by = 10
    ordering = ['user']

    def test_func(self):
        return self.request.user.is_company
    
    def handle_no_permission(self):
        return redirect('home:home')

    def get_company(self):
        if self.request.user.is_employee:
            employee = Employee.objects.get(user=self.request.user)
            self.company = employee.company
        elif self.request.user.is_company:
            company = Company.objects.get(user=self.request.user)
            self.company = company 

    def get_context_data(self, **kwargs):
       
        print(self.request.user.is_company)
        return super().get_context_data(**kwargs)
    
    def get_object(self,queryset=None):
        obj = super(ListEmployees, self).get_object(queryset=queryset)
        return obj
    
    
    



