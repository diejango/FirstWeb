from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import  newDepartamentoForm
from django.urls import reverse_lazy

from aplications.empleados.models import Empleado 
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "listdepa"


class NewDepartamentoView(FormView):
    template_name='departamento/new_departamento.html'
    form_class = newDepartamentoForm
    success_url=reverse_lazy('persona_app:correcto')
    
    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shorname=form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido =form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1', 
            departamento=depa

        )

        return super(NewDepartamentoView,self).form_valid(form)
        