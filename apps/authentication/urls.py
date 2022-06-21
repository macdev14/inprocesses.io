# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, CompanySignUpView, EmployeeSignUpView, password_reset_request
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView

# register_company, register_employee, 

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', CompanySignUpView.as_view(), name="register"),
    path('register/employee', EmployeeSignUpView.as_view(), name="register-employee"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/reset/auth-reset-pass-done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/reset/auth-reset-pass-confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/reset/auth-reset-pass-complete.html'), name='password_reset_complete'), 
    path("password_reset", password_reset_request, name="password_reset")
    #path('activate/<uidb64>/<token>/', activate_account, name='activate')

]

