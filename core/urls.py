# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    # ADD NEW Routes HERE
    path("serviceorders/", include("apps.serviceorder.urls") , name="serviceorder"),
    path("subserviceorder/", include("apps.subserviceorder.urls") , name="subserviceorder"),
    path("item/", include("apps.item.urls") , name="item"),
    path("process/", include("apps.process.urls") , name="process"),
    path("employee/", include("apps.employee.urls"), name="employee" ),
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    
    path("", include("apps.inprocesses.urls"))
]
