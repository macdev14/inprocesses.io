from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

class CreateEmployeePermission(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
       
        return self.request.user.is_company or self.request.user.is_superuser
        

    def handle_no_permission(self):
        return redirect('authentication:register')

class CreateCompanyPermission(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        print(self.request.user.is_company)
        return self.request.user.is_company or self.request.user.is_superuser
        

    def handle_no_permission(self):
        return redirect('home:home')