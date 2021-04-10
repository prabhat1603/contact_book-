from django.urls import path
from . import views

app_name = "contactapp"

urlpatterns = [

  path('autosuggest/', views.Autosuggest, name = 'autosuggest'),
  path('contactdetail/<int:pk>', views.ContactDetail, name = 'contactdetail'),
  path('updatecontact/<int:pk>', views.UpdateContact, name = 'updatecontact'),
  path('deletecontact/<int:pk>', views.DeleteContact, name = 'deletecontact'),
]
