from django.urls import path
from .views import CreateProcess, UpdateProcess, ListProcess
app_name='process'
urlpatterns = [
    # create views
    path('add', CreateProcess.as_view() ,name='add'),
    # update views
    path('update/<int:pk>', UpdateProcess.as_view() ,name='update'),
    # list views
    path('', ListProcess.as_view() , name="list"),
    

]