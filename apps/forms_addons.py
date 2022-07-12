from .serviceorder.forms import *
#from .permissions import EmployeePermission
from apps.serviceorder.models import *
# Create your views here.



class CompanyAddonForm(forms.ModelForm):
    company = None

    

    def get_company(self):
        if self.request.user.is_employee:
            employee = Employee.objects.get(user=self.request.user)
            self.company = employee.company
        elif self.request.user.is_company:
            company = Company.objects.get(user=self.request.user)
            self.company = company 