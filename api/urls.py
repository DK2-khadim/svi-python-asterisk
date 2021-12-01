from django.urls import path
from api import views

urlpatterns = [
    path('consultation/<int:numero>/<int:code>', views.getMontant, name="consultation"),
    path('transfert/<int:numero>/<int:code>/<int:dest>/<int:montant>', views.transfertCredit, name="transfert")
]
