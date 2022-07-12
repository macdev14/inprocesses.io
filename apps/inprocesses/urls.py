from django.urls import path

from .views import ListServiceOrderHistory
urlpatterns = [
    # create views
    #path('add', CreateServiceOrder.as_view() ,name='add-serviceorders'),
    # update views
    #path('update', UpdateServiceOrder.as_view() ,name='update-serviceorders'),
    # list views
    #path('processes', ListProcesses.as_view() , name="list-processes"),
    path('', ListServiceOrderHistory.as_view() ,name='list-serviceorders'),
    #path('subserviceorders', ListSubServiceOrders.as_view() ,name='list-subserviceorders'),

]