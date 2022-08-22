from django.shortcuts import render
from Apps.Users.models import Cliente
from django.http import HttpResponse

# Create your views here.

def Inicio(request):
    clilist = Cliente.objects.all()
    context = {
        'clilist' : clilist 
    }
    return render(request,'index.html', context)    
