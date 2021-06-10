from django.contrib import admin
from .models import Empleado,Cliente,D_tarjeta,C_tarjeta

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(D_tarjeta)
admin.site.register(C_tarjeta)