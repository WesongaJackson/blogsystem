from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("edit/<int:pk>/", views.edit, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),

]
