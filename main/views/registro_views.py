from django.http import  HttpResponse
from django.template import Template,Context,loader
from django.shortcuts import render

# el comportamiento actual es :iniciar sesion -> home
# 
# falta especificar distintos comportamientos (Aux de forms):
# get ->renderizar template 
# post-> validar usuario si no  ofrecer opcion de registrarse
# Renzo: copie y pegue la vista de login, aca hay que agregar mas cosas.

def registro(request):
    template=loader.get_template("registro.html")
    ctx={}
    rendered_template=template.render(ctx)
    return HttpResponse(rendered_template)