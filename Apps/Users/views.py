from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .forms import RawClienteForm,RawInstructorForm
# Create your views here.

def ClienteShowObject(request,myID):
    obj = Cliente.objects.get(id = myID)
    context = {
        'obj':obj,
        }
    
    return render(request, 'descripcion.html', context)

def UserCreateView(request):
    formCliente = RawClienteForm()
    formInstructor = RawInstructorForm()

    if request.method == "POST":
        formCliente = RawClienteForm(request.POST)
        if formCliente.is_valid():
            print(formCliente.cleaned_data)
            Cliente.objects.create(**formCliente.cleaned_data)
        else:
            print(formCliente.errors)
    
    if request.method == "POST":
        formInstructor = RawInstructorForm(request.POST)
        if formInstructor.is_valid():
            print(formInstructor.cleaned_data)
            Cliente.objects.create(**formInstructor.cleaned_data)
        else:
            print(formInstructor.errors)
    
    context = {
        'formCliente': formCliente,
        'formInstructor': formInstructor,
    }
    return render(request, 'users/clientcreate.html',context)


