from django.shortcuts import render, redirect
from .models import Appointment, Report
from .forms import AppointmentForm, HealthMetricsForm
import pandas as pd
from .medication_interactions import check_medication_interaction


def medication_interaction_view(request):
    if request.method == 'POST':
        med_list_a = request.POST.getlist('med_list_a[]')
        med_list_b = request.POST.getlist('med_list_b[]')

        result = check_medication_interaction(med_list_a, med_list_b)
        return render(request, 'interaction_result.html', {'result': result})

    return render(request, 'interaction_form.html')


def ddi(request):
    if request.method == 'POST':
        med_list_a = request.POST.getlist('med_list_a[]')
        med_list_b = request.POST.getlist('med_list_b[]')

        result = check_medication_interaction(med_list_a, med_list_b)
        return render(request, 'ddi.html', {'result': result})
    else:
        return render(request, 'ddi.html', {'result': None})


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def medication(request):
    return render(request, 'medication.html') 

def prescription(request):
    return render(request, 'prescription.html')

def ddi(request):
    return render(request, 'ddi.html')

def reports(request):
    return render(request, 'reports.html') 

def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments.html', {'form': form}) 

def reports_view(request):
    reports = Report.objects.all() 
    return render(request, 'reports.html', {'reports': reports})


def health_tracker_view(request):
    if request.method == 'POST':
        form = HealthMetricsForm(request.POST)
        if form.is_valid():
            blood_pressure = form.cleaned_data['blood_pressure']
            heart_rate = form.cleaned_data['heart_rate']
            sugar_levels = form.cleaned_data['sugar_levels']
            return redirect('health_tracker')  
    else:
        form = HealthMetricsForm()

    health_data = [
        {'blood_pressure': '120/80', 'heart_rate': '75', 'sugar_levels': '100'},
        {'blood_pressure': '130/85', 'heart_rate': '80', 'sugar_levels': '110'},
    ]

    context = {
        'form': form,
        'health_data': health_data,  
    }
    return render(request, 'health_tracker.html', context)


def medication_interaction_view(request):
    if request.method == 'POST':
        med_list_a = request.POST.getlist('med_list_a[]')
        med_list_b = request.POST.getlist('med_list_b[]')

        result = check_medication_interaction(med_list_a, med_list_b)
        return render(request, 'interaction_result.html', {'result': result})

    return render(request, 'interaction_form.html')
