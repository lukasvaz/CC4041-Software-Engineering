from django.shortcuts import render, redirect
from main.models import Incomes, Outcomes, AccountStatus
from igs.forms import TransactionForm
from django.http import HttpRequest
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required



@cache_control(private=True,no_cache=True, must_revalidate=True, no_store=True)
@login_required()
def transaction(request: HttpRequest):
    """(`POST`) Save the transaction (income/outcome) in database and redirect to the homepage.
    (`GET`) render the template form for add a new transaction.Disabling cache to ensure privacy
    """
    if request.method == "POST":
        user = request.user

        transaction_type = request.POST['tipo']
        amount = request.POST['monto']
        date_set = request.POST['fecha']
        category = request.POST['categoria']
        custom_category = request.POST.get('custom_categoria')
        descr = request.POST['description']

        account_status = AccountStatus.objects.get(user=user)

        if category == "otros" and custom_category:
            category = custom_category

        if "ingreso" == transaction_type:
            income = Incomes(account_status=account_status,
                             income=int(amount),
                             category=category,
                             set_at=date_set,
                             description=descr)
            income.save()

            income.update_balance()

        elif "egreso" == transaction_type:
            outcome = Outcomes(account_status=account_status,
                               outcome=int(amount),
                               category=category,
                               set_at=date_set,
                               description=descr)
            outcome.save()
            outcome.update_balance()

        return redirect("/home")

    elif request.method == "GET":
        form = TransactionForm()
        return render(request, 'transaccion.html', {'form': form})
