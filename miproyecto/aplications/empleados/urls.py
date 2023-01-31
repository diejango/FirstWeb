from django.urls import path
from . import views

app_name = 'persona_app'
urlpatterns = [
    
    path('list_all',views.ListAllEmpleados.as_view(),name='empleadosver'),
    path('list_area/<name>/',views.listByAreaEmpleado.as_view(),name='departamentodetail'),
    path('list_admin',views.ListAllEmpleadosadmin.as_view(),name='empleadosadmin'),
    path('list_kword',views.listByKword.as_view()),
    path('list_abilities',views.listAbilities.as_view()),
    path('ver_empleado/<pk>/',views.EmpleadoDetailView.as_view(),name='verdetalle'),
    path('add_empleado',views.EmpleadoCreateView.as_view(),name='add'),
    path('succes',views.succesView.as_view(),name='correcto'),
    path('update_empleado/<pk>/',views.EmpleadoUpdateView.as_view(),name='modificar'),
    path('delete_empleado/<pk>/',views.EmpleadoDeleteView.as_view(),name='eliminar'),
    path('',views.InicioView.as_view(),name='Inicio'),

]
