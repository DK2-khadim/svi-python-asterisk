from django.shortcuts import render, HttpResponse
from .models import Client
from rest_framework.response import Response
from gtts import gTTS
import os


def convertMp3toGsm(filename):
    print(os.path.basename)
    os.system(f"sox sounds/{filename}.mp3 -r 8000 -c 1 /usr/share/asterisk/sounds/{filename}.gsm")

def translate(text, language, filename):
    vocal = gTTS(text=text, lang=language, slow=False)
    vocal.save(f"./sounds/{filename}.mp3")
    convertMp3toGsm(filename)    


def getMontant(request, numero, code):
    text = ""
    montant = 0
    try:
        client = Client.objects.get(numero=numero)
        if client.codeSecret == code:
            text = f"Votre solde est de {client.solde}. Merci d'avoir utilisé DIC2 Service !"
            montant = client.solde
        else:
            text = "Le code est incorrect" 
    except Client.DoesNotExist:
        text = "Le numéro n'existe pas"

    translate(text, 'fr', numero)
    return HttpResponse(montant) 


def transfertCredit(request, numero, code, dest, montant):
    text = ""
    try:
        client = Client.objects.get(numero=numero)
        destinataire = Client.objects.get(numero=dest)
        if client.codeSecret == code:
            if client.solde >= montant:
                client.solde -= montant
                destinataire.solde += montant

                client.save()
                destinataire.save()
                text = f"Vous avez transféré avec succès {montant} au numéro {destinataire.numero}. Merci d'avoir utilisé DIC2 Service !"
            else:
                text = f"Votre solde est insuffisant. Merci de recharger votre compte !"
        else:
            text = "Le code est incorrect" 
    except Client.DoesNotExist:
        text = "Le numéro n'existe pas"

    translate(text, 'fr', numero)
    return HttpResponse(montant) 


# translate("Appuyez sur 1 pour consulter votre solde. Appuyez sur 2 pour faire un transfert de crédit.", "fr", "menu")
# translate("Bienvenue chez DIC2 Service", "fr", "bienvenu")
# translate("Veuillez entrer votre code secret", "fr", "codeSecret")
# translate("Veuillez entrer le numéro du destinataire", "fr", "numeroDest")
# translate("Veuillez entrer le montant du transfert.", "fr", "montantTrans")
# translate("Veuillez entrer le numéro du destinataire", "fr", "numeroDest")
# translate("Veuillez entrer le montant du transfert.", "fr", "montantTrans")