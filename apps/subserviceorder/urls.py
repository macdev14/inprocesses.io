from django.urls import path

from .views import CreateSubServiceOrder, UpdateSubServiceOrder, ListSubServiceOrders
app_name='subserviceorder'
urlpatterns = [
    # create views
    path('add', CreateSubServiceOrder.as_view() ,name='add-serviceorders'),
    # update views
    path('update', UpdateSubServiceOrder.as_view() ,name='update-serviceorders'),
    # list views
    #path('processes', ListProcesses.as_view() , name="list-processes"),
    path('', ListSubServiceOrders.as_view() ,name='list-serviceorders'),
    #path('subserviceorders', ListSubServiceOrders.as_view() ,name='list-subserviceorders'),

]