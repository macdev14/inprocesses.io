from django.shortcuts import redirect, render
from ..subserviceorder.forms import SubServiceOrderForm
from ..subserviceorder.models import SubServiceOrder

from apps.views_addons import CompanyAddonCreateView, CompanyAddonListView, CompanyAddonUpdateView

# Create your views here.


class UpdateSubServiceOrder(CompanyAddonUpdateView):
    form_class = SubServiceOrderForm
    
    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'sub-service-order'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ListSubServiceOrders(CompanyAddonListView):

    model = SubServiceOrder
    template_name = 'serviceordercontrol/subserviceorders/list-subserviceorders.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_queryset(self):
        self.get_company()
        if not 'pk' in self.request.resolver_match.kwargs:
            return redirect('serviceorder:add')
        if SubServiceOrder.objects.filter(main_os=self.request.resolver_match.kwargs['pk'], company=self.company).exists():
            return SubServiceOrder.objects.filter(main_os=self.request.resolver_match.kwargs['pk'], company=self.company)
        else:
            return redirect('')

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'sub-service-order'
        return super().get_context_data(**kwargs)

class CreateSubServiceOrder(CompanyAddonCreateView):
    form_class = SubServiceOrderForm
    template_name = 'serviceordercontrol/subserviceorders/add-subserviceorders.html'

    def get_context_data(self, **kwargs):
        kwargs['segment'] = 'sub-service-order'
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs