from django import forms
from .models import Empleado,Cliente,C_tarjeta,D_tarjeta

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["name","l_names","superior_id","sex","b_date"]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["name","l_names","works_with","sex","b_date","ct_id","dt_id"]

class D_tarjetaForm(forms.ModelForm):
    class Meta:
        model = D_tarjeta
        fields = ["num_tarjeta","balance","fecha_valida","cliente_id"]

class C_tarjetaForm(forms.ModelForm):
    class Meta:
        model = C_tarjeta
        fields = ["num_tarjeta","credito","c_disponible","saldo","dia_corte","fecha_valida","cliente_id"]

class del_objectForm(forms.Form):
    object_id = forms.IntegerField()