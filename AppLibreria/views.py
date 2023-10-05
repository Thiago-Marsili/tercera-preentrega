from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "AppLibreria/index.html")

def empleados(request):
    return render(request, "AppLibreria/empleados.html", {'empleados': Empleado.objects.all()})

def libros(request):
    return render(request, "AppLibreria/libros.html", {'libros': Libro.objects.all()})

def clientes(request):
    return render(request, "AppLibreria/clientes.html", {'clientes': Cliente.objects.all()})

def clientes_habu(request):
    
    if request.method == 'POST':
        
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            cliente = Cliente(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            
            cliente.save()
            
            return render(request, "AppLibreria/index.html")
    else:
        form = ClienteForm()
    
    return render(request, "AppLibreria/clientes_habu.html", {'form': form})

def empleados_habu(request):
    
    if request.method == 'POST':
        
        form = EmpleadoForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            empleado = Empleado(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], cargo=info['cargo'])
            
            empleado.save()
            
            return render(request, "AppLibreria/index.html")
    else:
        form = EmpleadoForm()
    
    return render(request, "AppLibreria/empleados_habu.html", {'form': form})

def libros_habu(request):
    
    if request.method == 'POST':
        
        form = LibroForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            libro = Libro(nombrel=info['nombrel'], descripcion=info['descripcion'])
            
            libro.save()
            
            return render(request, "AppLibreria/index.html")
    else:
        form = LibroForm()
    
    return render(request, "AppLibreria/libros_habu.html", {'form': form})

def response(request):
    try:
        if request.GET['email']:
            
            email = request.GET['email']
            clientesf = Cliente.objects.filter(email__icontains=email)
            
            return render(request, 'AppLibreria/response.html', {'clientes': clientesf, 'email': email, 'type': 'clientes'})
    except:
        pass
    try:
        if request.GET['cargo']:
            
            cargo = request.GET['cargo']
            empleadof = Empleado.objects.filter(cargo__icontains=cargo)
            
            return render(request, 'AppLibreria/response.html', {'empleados': empleadof, 'cargo': cargo, 'type': 'empleados'})
    except:
        pass

    try:
        if request.GET['nombrel']:
            
            nombrel = request.GET['nombrel']
            librof = Libro.objects.filter(nombrel__icontains=nombrel)
            
            return render(request, 'AppLibreria/response.html', {'libros': librof, 'nombrel': nombrel, 'type': 'libros'})
    except:
        pass
    
    respuesta = 'ERROR, data was not found'
    
    return HttpResponse(respuesta)
