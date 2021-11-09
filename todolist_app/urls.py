from django.urls import path
from . import views
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update-Task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete-Task'),
    #path('output/<str:pk>/', views.export_takslist, name= 'ex_tasklist'),
    path('export_csv', views.export_csv),
    path('importcsv/', views.import_csv, name='import-csv'),
    path('admin/', admin.site.urls),
    path('export_json', views.export_json, name='export-json'),
    path('table_todos/', views.tabletodo, name='table-todo')
]