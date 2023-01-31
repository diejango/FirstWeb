from django.urls import path
from . import views
app_name = 'departamento_app'
urlpatterns = [
    
    path('departamento_list',views.DepartamentoListView.as_view(),name='listardepa'),
    path('new_departamento',views.NewDepartamentoView.as_view(),name='nuevo_departamento'),

]