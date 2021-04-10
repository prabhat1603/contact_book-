from django.shortcuts import redirect, render
from contactapp.models import ContactBook
from contactapp.forms import RegisterForm
from django.contrib import messages



def Register(request):
    registerform = RegisterForm()
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, "Contact created successfully!")
            return redirect("login")
    context = {
      'registerform' : registerform
    }
    return render(request, "register.html", context)
