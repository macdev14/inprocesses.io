from .views import ListEmployees
from django.urls import path
app_name='employee'
urlpatterns = [
path('', ListEmployees.as_view(), name='list'),
]