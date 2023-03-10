from django.contrib import admin
from .models import Empleado,abilitie
# Register your models here.

admin.site.register(abilitie)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name 

    search_fields=('first_name',)
    list_filter=('job','abilities')
    filter_horizontal = ('abilities',)
admin.site.register(Empleado,EmpleadoAdmin)