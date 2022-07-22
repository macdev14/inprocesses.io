from django.urls import path
from .views import CreateItem, UpdateItem, ListItem
app_name='item'
urlpatterns = [
    # create views
    path('add', CreateItem.as_view() ,name='add'),
    # update views
    path('update/<int:pk>', UpdateItem.as_view() ,name='update'),
    # list views
    path('', ListItem.as_view() , name="list"),
    

]