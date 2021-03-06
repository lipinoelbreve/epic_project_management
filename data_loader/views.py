""" DATA LOADER VIEWS """
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from . import forms
from definitions.models import Stage
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *

def components(request):
    components_values = Component.objects.order_by('id')
    context = {'components':components_values}
    return render(request, 'data_loader/components.html', context)

def edit_component(request, id):
    component = Component.objects.get(pk=id)
    form = forms.CreateComponent(request.POST or None, instance=component)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:components')
    else:
        return render(request, 'data_loader/edit_component.html', {'form':form})

def load_component(request):
    if request.method == 'POST':
        form = forms.CreateComponent(request.POST)
        if form.is_valid():
            repeat = request.POST['repeat']
            if repeat == '':
                repeat = 1
            else:
                repeat = int(repeat)
            instance = form.save(commit=False)
            for i in range(repeat):
                instance.pk = None
                instance.save()
            return redirect('data_loader:components')
    else:
        form = forms.CreateComponent()
    return render(request, 'data_loader/load_component.html', {'form':form})

def systems(request):
    systems_values = System.objects.order_by('id')
    context = {'systems':systems_values}
    return render(request, 'data_loader/systems.html', context)

def edit_system(request, id):
    system = System.objects.get(pk=id)
    form = forms.CreateSystem(request.POST or None, instance=system)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:systems')
    else:
        return render(request, 'data_loader/edit_system.html', {'form':form})

def load_system(request):
    if request.method == 'POST':
        form = forms.CreateSystem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:systems')
    else:
        form = forms.CreateSystem()
    return render(request, 'data_loader/load_system.html', {'form':form})

def projects(request):
    projects_values = Project.objects.order_by('id')
    context = {'projects':projects_values}
    return render(request, 'data_loader/projects.html', context)

def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = forms.CreateProject(request.POST or None, instance=project)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:projects')
    else:
        return render(request, 'data_loader/edit_project.html', {'form':form})

def load_project(request):
    if request.method == 'POST':
        form = forms.CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:projects')
    else:
        form = forms.CreateProject()
    return render(request, 'data_loader/load_project.html', {'form':form})

def persons(request):
    persons_values = Person.objects.order_by('id')
    context = {'persons':persons_values}
    return render(request, 'data_loader/persons.html', context)

def edit_person(request, id):
    person = Person.objects.get(pk=id)
    form = forms.CreatePerson(request.POST or None, instance=person)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:persons')
    else:
        return render(request, 'data_loader/edit_person.html', {'form':form})

def load_person(request):
    if request.method == 'POST':
        form = forms.CreatePerson(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:persons')
    else:
        form = forms.CreatePerson()
    return render(request,'data_loader/load_person.html', {'form':form})

def load_supplier(request):
    if request.method == 'POST':
        form = forms.CreateSupplier(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_loader:suppliers')
    else:
        form = forms.CreateSupplier()
    return render(request,'data_loader/load_supplier.html', {'form':form})

def edit_supplier(request, id):
    supplier = Supplier.objects.get(pk=id)
    form = forms.CreateSupplier(request.POST or None, instance=supplier)
    if request.method == 'POST':
        form.save()
        return redirect('data_loader:suppliers')
    else:
        return render(request, 'data_loader/edit_supplier.html', {'form':form})

def suppliers(request):
    suppliers_values = Supplier.objects.order_by('id')
    context = {'suppliers':suppliers_values}
    return render(request, 'data_loader/suppliers.html', context)

# AJAX
def load_stages(request):
    track_id = request.GET.get('track_id')
    stages = Stage.objects.filter(track_id=track_id).all()
    return render(request, 'data_loader/stage_dropdown.html', {'stages': stages})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

class get_components(APIView):
    def get(self, request):
        components = Component.objects.all()
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_systems(APIView):
    def get(self, request):
        systems = System.objects.all()
        serializer = SystemSerializer(systems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class get_projects(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_persons(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)