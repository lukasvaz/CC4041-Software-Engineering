from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def register_user(request):
    if request.method == 'GET':
        return render(request, "main/register.html")
    
    elif request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        password=password)
        
        # This is not implemented yet
        # return HttpResponseRedirect("/account_status")