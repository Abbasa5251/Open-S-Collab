from django.urls import path
from . import views


urlpatterns = [
    path("", views.ViewProjects.as_view()),
    path("create/", views.CreateProject.as_view()),
]
