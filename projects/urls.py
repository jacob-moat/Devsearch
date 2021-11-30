from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('Project/<str:pk>/', views.Project, name = 'Project'),
    path('create-project/', views.createProject, name = 'create-project'),
    path('update-project/<str:pk>/', views.updateProject, name = 'update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name = "delete-project"),
]