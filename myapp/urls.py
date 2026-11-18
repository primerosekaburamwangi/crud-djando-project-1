# app - urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path("Add/", views.AddUser, name="user_add"),
    path("Edit/<int:id>/", views.EditUser, name="user_edit"),
    path("Delete/<int:eid>/", views.DeleteUser, name="user_delete"),
    path("View/<int:eid>/", views.ViewUser, name="user_view"),
]
