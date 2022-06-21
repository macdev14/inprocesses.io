# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from localflavor.br.forms import *
from django.db import transaction
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuário",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))




class CompanySignUpForm(UserCreationForm):

    cnpj = BRCNPJField(label='CNPJ', widget=forms.TextInput( attrs={'class': 'form-control', 
    'placeholder': 'CNPJ', 'id':'floatingInput cnpj',
    'onchange': 'cnpjlog(this);'} ) )

    name = forms.CharField(label='Razão Social', max_length=300, min_length=2, required=True, help_text='Required: First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razão Social'}))
    
  

    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Usuário",
    #             "class": "form-control"
    #         }
    #     ))

    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder": "Email",
    #             "class": "form-control"
    #         }
    #     ))
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Senha",
    #             "class": "form-control"
    #         }
    #     ))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Confirmar Senha",
    #             "class": "form-control"
    #         }
    #     ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('cnpj', 'name','username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(user=user, cnpj=self.cleaned_data.get('cnpj'), name=self.cleaned_data.get('name'))
        # company.add(*self.cleaned_data.get('cnpj'))
        # company.add(*self.cleaned_data.get('name'))
        return user

class EmployeeSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EmployeeSignUpForm, self).__init__(*args, **kwargs)

    cpf = BRCPFField(label='CPF', widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'CPF',
    'id':'floatingInput cnpj',
    'onchange': 'cnpjlog(this);'
    } ))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('cpf', 'username', 'email', 'password1', 'password2')
        #fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee= True
        user.save()
        employee = Employee.objects.create(user=user, company=self.user, cpf=self.cleaned_data.get('cpf'))
        #employee.cpf.add(*self.cleaned_data.get('cpf'))
        return user