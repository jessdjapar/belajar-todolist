from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('registration/login', LoginView.as_view(), name='login-user'),
    path('list', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update-Task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete-Task'),
    #path('output/<str:pk>/', views.export_takslist, name= 'ex_tasklist'),
    path('export_csv', views.export_csv, name='export-csv'),
    path('importcsv/', views.import_csv, name='import-csv'),
    #path('admin/', admin.site.urls),
    path('export_json', views.export_json, name='export-json'),
    path('', views.tabletodo, name='table-todo'),
    path('export_excel', views.export_excel, name='export-excel'),
    path('new_task', views.new_Task, name='new-Task')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)