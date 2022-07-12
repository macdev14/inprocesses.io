from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

class EmployeePermission(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
       
        return self.request.user.is_employee or self.request.user.is_superuser
        

    def handle_no_permission(self):
        return redirect('home:home')

class NotEmployeePermission(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_company
        #return False
        

    def handle_no_permission(self):
        return redirect('home:home')