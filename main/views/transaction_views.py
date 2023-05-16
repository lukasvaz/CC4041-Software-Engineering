from django.shortcuts import render, redirect
from main.models import Incomes, Outcomes, AccountStatus

# views transacciones
def transaction(request):
    if request.method == "POST":
        user = request.user

        transaction_type = request.POST['tipo']
        mount = request.POST['monto']
        date_set = request.POST['fecha']
        category = request.POST['categoria']

        account_status = AccountStatus.objects.get(user=user)

        if "ingreso" == transaction_type:
            income = Incomes(account_status=account_status,
                            income=mount,
                            category=category,
                            set_at=date_set,
                            description="")
            income.save()
        
        elif "egreso" == transaction_type:
            outcome = Outcomes(account_status=account_status,
                                outcome=mount,
                                category=category,
                                set_at=date_set,
                                description="Egreso")
            outcome.save()
        
        return redirect("/home")

    elif request.method == "GET":
        return render(request, 'transaccion.html')

