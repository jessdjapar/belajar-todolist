from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.db import connection
import csv
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'todolist_app/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'todolist_app/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    form = TaskForm(instance=item)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'todolist_app/delete.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['title', 'complete', 'created'])

    for t in Task.objects.all().values_list('title', 'complete','created'):
        writer.writerow(t)
    
    response['Content-Disposition'] = 'attachment; filename="Task.csv"'
    return response

def import_csv(request):
    res = HttpResponse("OK")
    print(res)
    template = "importcsv.html"
    if request.method == "GET":
        return render(request, template)
    
    csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    return render(request, 'todolist_app/importcsv.html')
