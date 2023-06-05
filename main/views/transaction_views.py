from django.shortcuts import render, redirect
from main.models import Incomes, Outcomes, AccountStatus
from igs.forms import TransactionForm

# views transacciones

##view for the transactions form , if request is GET method render the template  
#if its POST save transaction in database
def transaction(request):
    if request.method == "POST":
        user = request.user

        transaction_type = request.POST['tipo']
        mount = request.POST['monto']
        date_set = request.POST['fecha']
        category = request.POST['categoria']
        custom_category = request.POST.get('custom_categoria')  # Get the custom category value

        account_status = AccountStatus.objects.get(user=user)

        if category == "otros" and custom_category:
                category = custom_category

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
        form = TransactionForm()
        return render(request, 'transaccion.html', {'form' : form})

