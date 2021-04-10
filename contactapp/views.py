from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from .models import ContactBook
from .forms import ContactForm
import json
# Create your views here.

@login_required
def Index(request):
    contacts = ContactBook.objects.all()
    if request.GET.get("searched"):
        contacts = ContactBook.objects.filter(name__username=request.GET.get("searched"))
        if not contacts:
            contacts = ContactBook.objects.filter(name__email=request.GET.get("searched"))
        else:
            messages.success(request, "No result found!")
        return render(request, 'contactapp/contactdetail.html', {'mydetail' : contacts[0]})
    return render(request, 'contactapp/index.html', {'contacts' : contacts})

def Autosuggest(request):
    if request.GET:
        queryterm = request.GET.get("term")
        searchedname = ContactBook.objects.filter(name__username__icontains=queryterm)
        searchedemail = ContactBook.objects.filter(name__email__icontains=queryterm)
        searchedlist = []
        searchedlist += [ object.name.username for object in searchedname ]
        searchedlist += [ object.name.email for object in searchedemail ]
        return JsonResponse(searchedlist, safe=False)

def ContactDetail(request, pk):
    mydetail = ContactBook.objects.get(id=pk)
    permission = "no"
    if pk == ContactBook.objects.get(name=request.user).id:
        permission = "yes"
    return render(request, "contactapp/contactdetail.html", {'mydetail' : mydetail, "permission" : permission})

def UpdateContact(request, pk):
    contact = get_object_or_404(ContactBook, pk=pk)
    updateform = ContactForm(instance = contact)
    if request.method == "POST":
        updateform = ContactForm(request.POST,request.FILES, instance = contact)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, "Contact updated successfully!")
            return redirect(contact)
    context = {
     'updateform' : updateform
    }
    return render(request, "contactapp/updatecontact.html", context)
def DeleteContact(request, pk):
    contact = get_object_or_404(ContactBook, pk = pk)
    if contact.id == ContactBook.objects.get(name = request.user).id:
        User.objects.get(id = contact.name.id).delete()
        messages.success(request, "Contact deleted successfully!")
        return redirect("logout")
    return render(request, "contactapp/contactdetail.html", {'mydetail' : contact})
