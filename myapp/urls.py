from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [
    path("emp", views.createEmp),
    path("show", views.show),
    path("edit/<int:id>", views.edit),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.destroy),
]
