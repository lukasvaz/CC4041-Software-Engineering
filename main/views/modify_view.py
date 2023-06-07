from django.shortcuts import render, redirect
from django.http import HttpRequest
from main.models import Incomes, Outcomes


def modify_income(request: HttpRequest, id):
    """(`POST`) Modify the Income's fields by the new parameters given in the request form, uses the `id`
    parameter passed in the url to get the specific income, redirects to the homepage. (`GET`) Render the form template to modify
    the income entry.
    """

    if request.method == 'GET':
        return render(request, "modify_entry.html")

    elif request.method == 'POST':
        income_entry = Incomes.objects.get(pk=id)

        income_entry.income = request.POST['monto']
        income_entry.category = request.POST['categoria']
        income_entry.set_at = request.POST['fecha']
        income_entry.description = request.POST['descripcion']

        income_entry.save()

        return redirect("/home/")


def modify_outcome(request: HttpRequest, id):
    """(`POST`) Modify the Outcome's fields by the new parameters given in the request form, uses
    the `id` parameter passed by the url to get the specific outcome, redirects to the homepage. (`GET`) Render the form template to modify
    the outcome entry.
    """

    if request.method == 'GET':
        return render(request, "modify_entry.html")

    elif request.method == 'POST':
        outcome_entry = Outcomes.objects.get(pk=id)

        outcome_entry.outcome = request.POST['monto']
        outcome_entry.category = request.POST['categoria']
        outcome_entry.set_at = request.POST['fecha']
        outcome_entry.description = request.POST['descripcion']

        outcome_entry.save()

        return redirect("/home")
