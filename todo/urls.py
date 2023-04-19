from django.urls import path
from . import views

urlpatterns = [
    path("", views.apioverview, name="home"),
    path("task-list/", views.todo, name="list"),
    path("task-detail/<str:pk>/", views.tododetail, name="detail"),
    path("task-create/", views.todocreate, name="create"),
    path("task-update/<str:pk>/", views.todoupdate, name="update"),
    path("task-delete/<str:pk>/", views.tododelete, name="delete"),
]
