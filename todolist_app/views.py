from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.db import connection
import csv, io
from django.contrib import messages
from django.http import JsonResponse
import json

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

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['title', 'complete', 'created'])

    for t in Task.objects.all().values_list('title', 'complete','created'):
        writer.writerow(t)
    
    response['Content-Disposition'] = 'attachment; filename="Task.csv"'
    return response

def import_csv(request):
    template = "todolist_app/importcsv.html"
    csvdata = Task.objects.all()

    prompt = {'order': 'title, complete, created',
              'tasks': csvdata}

    if request.method =='GET':
        return render (request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    count = 0
    if count == 0:
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = Task.objects.update_or_create(
                title = column[0],
                complete = column[1],
                created = column[2]
            )
        count=count+1
        if count == 1:
            return redirect('/')

    context = {}
    return render(request, template, context)


def export_csv(request):
    response = HttpResponse(content_type='text/json')
    writer = csv.writer(response)
    writer.writerow(['title', 'complete', 'created'])

    for t in Task.objects.all().values_list('title', 'complete','created'):
        writer.writerow(t)
    
    response['Content-Disposition'] = 'attachment; filename="Task.csv"'
    return response

def export_json(request):
    jsondata = list(Task.objects.values())
    return JsonResponse(jsondata, safe=False, json_dumps_params={'indent': 2})

def tabletodo(request):
    tasks = Task.objects.all()
    return render(request, 'todolist_app/table_todos.html', 
        {'data': tasks})