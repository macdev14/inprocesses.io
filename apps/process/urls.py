from django.urls import path
from .views import CreateProcess, UpdateProcess, ListProcess
app_name='process'
urlpatterns = [
    # create views
    path('add', CreateProcess.as_view() ,name='add-serviceorders'),
    # update views
    path('update', UpdateProcess.as_view() ,name='update-serviceorders'),
    # list views
    path('', ListProcess.as_view() , name="list-processes"),
    

]