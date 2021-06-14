from django.shortcuts import render, redirect
from .models import Empleado,Cliente,D_tarjeta,C_tarjeta
from .forms import *
from django.contrib import messages
from random import randint
from datetime import date
import os

# Create your views here.

def generate_card():
    number = ""
    for n in range(16):
        number += str(randint(0,9))
    return number

def valid_trough(d,years):
    try:     
        return d.replace(year = d.year + years)
    except ValueError:      
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

#Linting error, nothing important
def home(request):
    all_employees = Empleado.objects.all
    return render(request,'home.html',{'all':all_employees})
    

def add_emp(request):
    all_employees = Empleado.objects.all
    if request.method == "POST":
        form = EmpleadoForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            l_names = request.POST['l_names']
            superior_id = request.POST['superior_id']
            sex = request.POST['sex']
            b_date = request.POST['b_date']
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'employee.html',{
                'name' : name,
                'l_names' : l_names,
                'superior_id' : superior_id,
                'sex' : sex,
                'b_date' : b_date,
                'all' : all_employees,
            })
        messages.success(request,"Empleado agregado correctamente")
        return redirect('employees')

    else:
        return render(request,'employee.html',{'all':all_employees})

def render_emp(request):
    all_employees = Empleado.objects.all
    return render(request,'employees.html',{'all':all_employees})

def add_client(request):
    all_employees = Empleado.objects.all
    if request.method == "POST":
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            l_names = request.POST['l_names']
            works_with = request.POST['works_with']
            sex = request.POST['sex']
            b_date = request.POST['b_date']
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'client.html',{
                'name' : name,
                'l_names' : l_names,
                'works_with' : works_with,
                'sex' : sex,
                'b_date' : b_date,
                'all' : all_employees,
            })
        messages.success(request,"Cliente agregado correctamente")
        return redirect('clients')

    else:
        return render(request,'client.html',{'all':all_employees})

def render_client(request):
    all_clients = Cliente.objects.all
    return render(request,'clients.html',{'all':all_clients})

def add_card(request):
    _mutable = request.POST._mutable
    request.POST._mutable = True
    # сhange the values you want
    request.POST['fecha_valida'] = valid_trough(date.today(),6)
    request.POST['num_tarjeta'] = generate_card()
    # set mutable flag back
    request.POST._mutable = _mutable

    all_clients = Cliente.objects.all
    if request.method == "POST":
        form = D_tarjetaForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            cliente_id = request.POST['cliente_id']
            balance = request.POST['balance']
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'card.html',{
                'cliente_id' : cliente_id,
                'balance' : balance,
                'all' : all_clients,
            })
        messages.success(request,"Tarjeta agregada correctamente")
        return redirect('card')

    else:
        return render(request,'card.html',{'all':all_clients})

def render_card(request):
    all_cards = D_tarjeta.objects.all
    return render(request,'cards.html',{'all':all_cards})

def add_ccard(request):
    _mutable = request.POST._mutable
    request.POST._mutable = True
    # сhange the values you want
    request.POST['fecha_valida'] = valid_trough(date.today(),6)
    request.POST['num_tarjeta'] = generate_card()
    request.POST['dia_corte'] = randint(1,25)
    # set mutable flag back
    request.POST._mutable = _mutable
    all_clients = Cliente.objects.all
    if request.method == "POST":
        _mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['c_disponible'] = request.POST['credito']
        request.POST._mutable = _mutable
        form = C_tarjetaForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            cliente_id = request.POST['cliente_id']
            credito = request.POST['credito']
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'ccard.html',{
                'cliente_id' : cliente_id,
                'credito' : credito,
                'all':all_clients,
            })
        messages.success(request,"Tarjeta agregada correctamente")
        return redirect('ccard')

    else:
        return render(request,'ccard.html',{'all':all_clients})

def render_ccard(request):
    all_ccards = C_tarjeta.objects.all
    return render(request,'ccards.html',{'all':all_ccards})

def delete_emp(request):
    all_employees = Empleado.objects.all
    if request.method == "POST":
        form = del_objectForm(request.POST or None)
        if form.is_valid():
            emp_to_delete = form.cleaned_data['object_id']
            try:
                emp = Empleado.objects.get(id = emp_to_delete)
                emp.delete()
            except:
                messages.success(request,"El ID del Empleado no existe")
                return render(request,'del_employee.html',{'all':all_employees})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'del_employee.html',{'all':all_employees})
        messages.success(request,"Empleado eliminado exitosamente")
        return redirect('employees')

    else:
        return render(request,'del_employee.html',{'all':all_employees})

def delete_client(request):
    all_clients = Cliente.objects.all
    if request.method == "POST":
        form = del_objectForm(request.POST or None)
        if form.is_valid():
            client_to_delete = form.cleaned_data['object_id']
            try:
                client = Cliente.objects.get(id = client_to_delete)
                client.delete()
            except:
                messages.success(request,"El ID del Cliente no existe")
                return render(request,'del_client.html',{'all':all_clients})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'del_client.html',{'all':all_clients})
        messages.success(request,"Cliente eliminado exitosamente")
        return redirect('clients')

    else:
        return render(request,'del_client.html',{'all':all_clients})

def delete_card(request):
    all_cards = D_tarjeta.objects.all
    if request.method == "POST":
        form = del_objectForm(request.POST or None)
        if form.is_valid():
            card_to_delete = form.cleaned_data['object_id']
            try:
                card = D_tarjeta.objects.get(id = card_to_delete)
                card.delete()
            except:
                messages.success(request,"El ID de la tarjeta no existe")
                return render(request,'del_card.html',{'all':all_cards})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'del_card.html',{'all':all_cards})
        messages.success(request,"Tarjeta de Débito eliminada exitosamente")
        return redirect('del_card')

    else:
        return render(request,'del_card.html',{'all':all_cards})

def delete_ccard(request):
    all_cards = C_tarjeta.objects.all
    if request.method == "POST":
        form = del_objectForm(request.POST or None)
        if form.is_valid():
            card_to_delete = form.cleaned_data['object_id']
            try:
                card = C_tarjeta.objects.get(id = card_to_delete)
                card.delete()
            except:
                messages.success(request,"El ID de la tarjeta no existe")
                return render(request,'del_ccard.html',{'all':all_cards})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'del_ccard.html',{'all':all_cards})
        messages.success(request,"Tarjeta de Débito eliminada exitosamente")
        return redirect('del_ccard')

    else:
        return render(request,'del_ccard.html',{'all':all_cards})

def s_queries(request):
    all_emp = Empleado.objects.raw('SELECT * FROM website_empleado;')
    all_clients = Cliente.objects.raw('SELECT * FROM website_cliente;')
    all_ccards = C_tarjeta.objects.raw('SELECT * FROM website_c_tarjeta;')
    all_cards = D_tarjeta.objects.raw('SELECT * FROM website_d_tarjeta;')
    emp_with_s = Empleado.objects.raw("SELECT id,name,l_names FROM website_empleado WHERE name LIKE %s OR l_names LIKE %s;",["S%","S%"])

    return render(request,'s_queries.html',{
        'all_emp':all_emp,
        'all_clients':all_clients,
        'all_ccards':all_ccards,
        'all_cards':all_cards,
        'emp_with_s':emp_with_s,
    })

def c_queries(request):
    purchase_10k = Cliente.objects.raw('''
            SELECT website_cliente.id,website_cliente.name,website_cliente.l_names,website_d_tarjeta.balance,website_d_tarjeta.balance - 10000 AS "complex"
            FROM website_cliente
            JOIN website_d_tarjeta
            ON website_cliente.dt_id_id = website_d_tarjeta.id;
    ''')
    c_anual = Cliente.objects.raw('''
            SELECT website_cliente.id,website_cliente.name,website_cliente.l_names,website_c_tarjeta.credito,(website_c_tarjeta.credito * .10 *12) * .02 AS "complex"
            FROM website_cliente
            JOIN website_c_tarjeta
            ON website_cliente.ct_id_id = website_c_tarjeta.id;
    ''')
    c_mensual = Cliente.objects.raw('''
            SELECT website_cliente.id,website_cliente.name,website_cliente.l_names,website_d_tarjeta.balance,(website_d_tarjeta.balance * .01) * 1.16 AS "complex"
            FROM website_cliente
            JOIN website_d_tarjeta
            ON website_cliente.dt_id_id = website_d_tarjeta.id;
    ''')
    c_card_7k = Cliente.objects.raw('''
            SELECT website_cliente.id,website_cliente.name,website_cliente.l_names,website_c_tarjeta.credito,website_c_tarjeta.c_disponible - 7500*1.16 AS "complex"
            FROM website_cliente
            JOIN website_c_tarjeta
            ON website_cliente.ct_id_id = website_c_tarjeta.id;
    ''')

    dep_3k = Cliente.objects.raw('''
            SELECT website_cliente.id,website_cliente.name,website_cliente.l_names,website_d_tarjeta.balance,website_d_tarjeta.balance + 3500 AS "complex"
            FROM website_cliente
            JOIN website_d_tarjeta
            ON website_cliente.dt_id_id = website_d_tarjeta.id;
    ''')

    return render(request,'c_queries.html',{
        'purchase_10k':purchase_10k,
        'c_anual':c_anual,
        'c_mensual':c_mensual,
        'c_card_7k':c_card_7k,
        'dep_3k':dep_3k,
    })

def a_queries(request):
    oldest = Empleado.objects.raw('''
            SELECT id,name,l_names,b_date
            FROM website_empleado
            WHERE b_date = (
                SELECT MIN(b_date)
                FROM website_empleado
            );
    ''')

    young = Empleado.objects.raw('''
            SELECT id,name,l_names,b_date
            FROM website_empleado
            WHERE b_date = (
                SELECT MAX(b_date)
                FROM website_empleado
            );
    ''')

    avg_b = D_tarjeta.objects.raw('''SELECT * FROM avg_dt''')

    sum_dt = D_tarjeta.objects.raw('''SELECT * FROM sum_dt''')

    emp_sex = Empleado.objects.raw('''SELECT * FROM emp_sex''')

    return render(request,'a_queries.html',{
        'oldest':oldest,
        'young':young,
        'avg_b':avg_b,
        'emp_sex':emp_sex,
        'sum_dt':sum_dt,
    })

def up_employee(request):
    all_employees = Empleado.objects.all
    if request.method == "POST":
        form = up_employeeForm(request.POST or None)
        if form.is_valid():
            object_id = form.cleaned_data['object_id']
            name = form.cleaned_data['name']
            l_names = form.cleaned_data['l_names']
            superior_id = form.cleaned_data['superior_id']
            sex = form.cleaned_data['sex']
            b_date = form.cleaned_data['b_date']
            try:
                Empleado.objects.filter(pk=object_id).update(name=name,l_names=l_names,superior_id=superior_id,sex=sex,b_date=b_date)
            except:
                messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
                return render(request,'up_employee.html',{'all':all_employees})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'up_employee.html',{'all':all_employees})
        messages.success(request,"Empleado modificado exitosamente")
        return redirect('employees')

    else:
        return render(request,'up_employee.html',{'all':all_employees})

def up_client(request):
    all_employees = Empleado.objects.all
    all_clients = Cliente.objects.all
    if request.method == "POST":
        form = up_clientForm(request.POST or None)
        if form.is_valid():
            object_id = form.cleaned_data['object_id']
            name = form.cleaned_data['name']
            l_names = form.cleaned_data['l_names']
            works_with = form.cleaned_data['works_with']
            sex = form.cleaned_data['sex']
            b_date = form.cleaned_data['b_date']
            try:
                Cliente.objects.filter(pk=object_id).update(name=name,l_names=l_names,works_with=works_with,sex=sex,b_date=b_date)
            except:
                messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
                return render(request,'up_client.html',{'all_c':all_clients,'all_e':all_employees})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'up_client.html',{'all_c':all_clients,'all_e':all_employees})
        messages.success(request,"Cliente modificado exitosamente")
        return redirect('clients')

    else:
        return render(request,'up_client.html',{'all_c':all_clients,'all_e':all_employees})

def up_card(request):
    all_cards = D_tarjeta.objects.all
    if request.method == "POST":
        form = up_cardForm(request.POST or None)
        if form.is_valid():
            object_id = form.cleaned_data['object_id']
            balance = form.cleaned_data['balance']
            try:
                D_tarjeta.objects.filter(pk=object_id).update(balance=balance)
            except:
                messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
                return render(request,'up_card.html',{'all':all_cards})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'up_card.html',{'all':all_cards})
        messages.success(request,"Tarjeta de Débito modificada exitosamente")
        return redirect('cards')

    else:
        return render(request,'up_card.html',{'all':all_cards})

def up_ccard(request):
    all_cards = C_tarjeta.objects.all
    if request.method == "POST":
        form = up_ccardForm(request.POST or None)
        if form.is_valid():
            object_id = form.cleaned_data['object_id']
            credito = form.cleaned_data['credito']
            c_disponible = form.cleaned_data['c_disponible']
            print(credito,type(credito))
            print(c_disponible,type(c_disponible))
            saldo = credito - c_disponible
            try:
                C_tarjeta.objects.filter(pk=object_id).update(credito=credito,saldo=saldo,c_disponible=c_disponible)
            except:
                messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
                return render(request,'up_ccard.html',{'all':all_cards})
        else:
            messages.success(request,"Ocurrió un error en el formulario! Por favor, intenta de nuevo...")
            return render(request,'up_ccard.html',{'all':all_cards})
        messages.success(request,"Tarjeta de Crédito modificada exitosamente")
        return redirect('ccards')

    else:
        return render(request,'up_ccard.html',{'all':all_cards})

def backup(request):
    os.popen("mysqldump -h127.0.0.1 -uroot -padmin > backup.sql")
    messages.success(request,"Base de datos respaldada")
    return render(request,'home.html',{})