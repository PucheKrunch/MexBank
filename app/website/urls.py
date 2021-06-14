from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('employee',views.add_emp, name="employee"),
    path('employees',views.render_emp, name="employees"),
    path('client',views.add_client, name="client"),
    path('clients',views.render_client, name="clients"),
    path('card',views.add_card, name="card"),
    path('cards',views.render_card, name="cards"),
    path('ccard',views.add_ccard, name="ccard"),
    path('ccards',views.render_ccard, name="ccards"),
    path('del_employee',views.delete_emp, name="del_employee"),
    path('del_client',views.delete_client, name="del_client"),
    path('del_card',views.delete_card, name="del_card"),
    path('del_ccard',views.delete_ccard, name="del_ccard"),
    path('s_queries',views.s_queries,name="s_queries"),
    path('c_queries',views.c_queries,name="c_queries"),
    path('a_queries',views.a_queries,name="a_queries"),
    path('up_employee',views.up_employee,name="up_employee"),
    path('up_client',views.up_client,name="up_client"),
    path('up_card',views.up_card,name="up_card"),
    path('up_ccard',views.up_ccard,name="up_ccard"),
] 