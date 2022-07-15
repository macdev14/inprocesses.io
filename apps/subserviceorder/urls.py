from django.urls import path

from .views import CreateSubServiceOrder, UpdateSubServiceOrder, ListSubServiceOrders
app_name='subserviceorder'
urlpatterns = [
    # create views
    path('add', CreateSubServiceOrder.as_view() ,name='add'),
    # update views
    path('update', UpdateSubServiceOrder.as_view() ,name='update'),
    # list views
    #path('processes', ListProcesses.as_view() , name="list-processes"),
    path('', ListSubServiceOrders.as_view() ,name='list'),
    #path('subserviceorders', ListSubServiceOrders.as_view() ,name='list-subserviceorders'),

]