from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_jobs, name='list'),
    path('create/', views.create_job, name='create'),
    path('update/<int:id>/', views.update_job, name='update'),
    path('delete/<int:id>/', views.delete_job, name='delete'),
    path('apply/<int:id>/',views.apply_job,name='apply'),
     
   
    
   
]
