from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update-Task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete-Task'),
    #path('output/<str:pk>/', views.export_takslist, name= 'ex_tasklist'),
    path('export_csv', views.export)
]