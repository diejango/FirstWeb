from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView

from .forms import EmpleadoForm
from .models import Empleado
from django.urls import reverse_lazy
# Create your views here.

class InicioView(TemplateView):
    template_name = "inicio.html"
    
class ListAllEmpleados (ListView):
    template_name = 'empleados/list_all.html'
    paginate_by=4
    ordering = 'id'
    #model = Empleado
    context_object_name='empleadost'
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        
        lista = Empleado.objects.filter(
            full_name__icontains= palabra_clave
        )     
        return lista

class ListAllEmpleadosadmin (ListView):
    template_name = 'empleados/list_admin.html'
    paginate_by=5
    model = Empleado
    ordering = 'id'
    context_object_name='empleadosa'
    

class listByAreaEmpleado (ListView):
    template_name = 'empleados/list_area.html'
    context_object_name='area'

    def get_queryset(self):
        
        area = self.kwargs['name']
        
        lista = Empleado.objects.filter(
            departamento__name= area
        )     
        return lista

class listByKword (ListView):
    template_name = 'empleados/list_kword.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )     
        return lista

class listAbilities(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name='habilidades'
    def get_queryset(self):
        x = self.request.GET.get('kword','')
        empleado=Empleado.objects.get(first_name = x)
        return empleado.abilities.all


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context =  super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context ['nombre'] = ' :  '
        return context


class succesView(TemplateView):
    template_name = "empleados/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    form_class=EmpleadoForm
    success_url= reverse_lazy('persona_app:empleadosadmin')
    def form_valid(self, form):
        empleado=form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    form_class=EmpleadoForm
    success_url= reverse_lazy('persona_app:empleadosadmin')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        empleado=form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView,self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url= reverse_lazy('persona_app:empleadosadmin')

       