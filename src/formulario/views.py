# Create your views here.

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render


from .models import Banco, Agencia

#CRUD Banco
def home_view(request):
    return render(request, 'formulario/home_page.html',) 
    

class BancoList(ListView):
    model = Banco
    queryset = Banco.objects.all()        

class BancoCreate(CreateView):
    model = Banco
    fields = '__all__'
    success_url = reverse_lazy('listBanco')

class BancoUpdate(UpdateView):
    model = Banco
    fields = '__all__'
    success_url = reverse_lazy('listBanco')

class BancoDelete(DeleteView):
    queryset = Banco.objects.all()
    success_url = reverse_lazy('listBanco')



#CRUD Agencia

class AgenciaList(ListView):
    model = Agencia
    queryset = Agencia.objects.all()        

class AgenciaCreate(CreateView):
    model = Agencia
    fields = '__all__'
    success_url = reverse_lazy('listAgencia')


class AgenciaUpdate(UpdateView):
    model = Agencia
    fields = '__all__'
    success_url = reverse_lazy('listAgencia')



class AgenciaDelete(DeleteView):
    queryset = Agencia.objects.all()
    success_url = reverse_lazy('listAgencia')

