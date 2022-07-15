# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from requests import request
from .forms import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import CreateView
from .permissions import CreateEmployeePermission, CreateCompanyPermission
from core.settings import EMAIL_HOST_USER
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages 
def check_admin(user):
    return user.is_superuser

def check_employee(user):
    return user.is_employee

def check_company(user):
    return user.is_company

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():
                for user in associated_users:
                    protocol = 'https' if request.is_secure() else 'http'
                    subject = "Alteração de Senha"
                    email_template_name = "accounts/reset/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain': request.META['HTTP_HOST'],
					'site_name': 'InProcesses',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': protocol,
					}
                    email = render_to_string(email_template_name, c)

                    
                    send_mail(subject, email, EMAIL_HOST_USER, [user.email], fail_silently=False)
                   
                    return redirect('/password_reset/done/')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/reset/auth-reset-pass-confirm-email.html", context={"password_reset_form":password_reset_form})
     

# def register_company(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = CompanySignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'Company created successfully.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = CompanySignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


# @login_required
# @user_passes_test(check_company)
# def register_employee(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = EmployeeSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'Company created successfully.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = EmployeeSignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


class CompanySignUpView(CreateCompanyPermission, CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'accounts/register.html'

    msg = None
    success = False

    #fields = '__all__'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'negócio'
        kwargs['msg'] = self.msg
        kwargs['success'] = self.success
        # print("test")
        print(super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin:index')


class EmployeeSignUpView(CreateEmployeePermission, CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = "employees/add-employee.html"
    #fields = '__all__'
    msg = None
    success = False

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(EmployeeSignUpView, self).get_form_kwargs(**kwargs)
        #form_kwargs["user"] = self.request.user
        usr = Company.objects.get(user=self.request.user)
        form_kwargs["company"] = usr
        return form_kwargs

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'colaborador'
        kwargs['msg'] = self.msg
        kwargs['success'] = self.success
        kwargs['user'] = self.request.user
        kwargs['segment'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if self.request.user.is_company:
            usr = Company.objects.get(user=self.request.user)
            form.company = usr
            user = form.save()
            self.msg = 'Employee created successfully.'
            messages.success(self.request,'Colaborador cadastrado com Sucesso.')
            self.success = True
            login(self.request, user)
            return redirect('home:home')
        else:
            self.msg = 'Please register company before registering employee.'
            self.success = False
            messages.error(self.request,'Cadastre uma empresa antes de cadastrar um colaborador.')
            # raise forms.ValidationError("Não é uma empresa")
            return redirect('authentication:register')