from django.shortcuts import render
from django.urls import reverse
from apps.item.models import Item
from .forms import ItemForm
from apps.views_addons import CompanyAddonListView, CompanyAddonCreateView, CompanyAddonUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
# Create your views here.

 
class ListItem(CompanyAddonListView):

    model = Item
    template_name = 'serviceordercontrol/item/list-item.html'
    paginate_by = 10
    ordering = ['number']

    def get_queryset(self):
        self.get_company() 
        print(Item.objects.filter(company=self.company))
        return Item.objects.filter(company=self.company)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)
    
    def get_object(self,queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    
class CreateItem(CompanyAddonCreateView):
    form_class = ItemForm
    model = Item
    template_name = 'serviceordercontrol/item/add-item.html'
    

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        self.get_company()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
       
        return reverse('item:list')

class UpdateItem(CompanyAddonUpdateView, UserPassesTestMixin):
    model = Item
    form_class = ItemForm
    template_name = 'serviceordercontrol/item/update-item.html'

    def dispatch(self, request, *args, **kwargs):
        # here you can make your custom validation for any particular user
        self.get_company()
        self.object = self.get_object()
        if not self.object.company == self.company:
            return reverse('item:list')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'item'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def get_success_url(self):
       
        return reverse('item:list')

    def get_permission_denied_message(self):
        return reverse('item:list')