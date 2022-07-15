from django.urls import path
from .views import CreateClient, UpdateClient, ListClient
app_name='client'
urlpatterns = [
    # create views
    path('add', CreateClient.as_view() ,name='add'),
    # update views
    path('update', UpdateClient.as_view() ,name='update'),
    # list views
    path('', ListClient.as_view() , name="list"),
    

]