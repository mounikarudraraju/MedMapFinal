import statistics
from django.urls import path
from HMS import views
from Telehealth import settings
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointments/', views.appointments, name='appointments'),
    path('medication/', views.medication, name='medication'),
    path('reports/', views.reports, name='reports'),
    path('reports/', views.reports_view, name='reports'),
    path('health-tracker/', views.health_tracker_view, name='Health Tracker'),
    path('health-tracker/', views.health_tracker_view, name='health_tracker'),
    path('prescription/', views.prescription, name='prescription'), 
    path('ddi/', views.ddi, name='ddi'), 
    path('medication_interaction/', views.medication_interaction_view, name='medication_interaction_view'), 

]
    


    


    

