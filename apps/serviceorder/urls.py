from django.urls import path

from .views import *
app_name='serviceorder'
urlpatterns = [
    # create views
    path('add', CreateServiceOrder.as_view() ,name='add'),
    # update views
    path('update', UpdateServiceOrder.as_view() ,name='update'),
    # list views
    #path('processes', ListProcesses.as_view() , name="list-processes"),
    path('', ListServiceOrders.as_view() ,name='list'),
    #path('subserviceorders', ListSubServiceOrders.as_view() ,name='list-subserviceorders'),

]