from django.urls import path

from .views import CreateSubItem, UpdateSubItem, ListSubItem
app_name='subitem'
urlpatterns = [
    # create views
    path('add', CreateSubItem.as_view() ,name='add'),
    # update views
    path('update', UpdateSubItem.as_view() ,name='update'),
    # list views
    #path('processes', ListProcesses.as_view() , name="list-processes"),
    path('', ListSubItem.as_view() ,name='list'),
    #path('subserviceorders', ListSubServiceOrders.as_view() ,name='list-subserviceorders'),

]