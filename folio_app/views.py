from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home (request):
    blogs= Blog.objects.all()
    my_folios= My_portfolio.objects.all()
    categories = Category.objects.all()
    
    context={
        'blogs': blogs,
        'my_folios': my_folios,
        'categories': categories 
    }
    return render (request, 'index.html', context)

def contact_view(request):
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        # Créer et sauvegarder l'objet Contact
        contact = Contact(prenom=prenom, nom=nom, email=email, sujet=sujet, message=message)
        contact.save()

         # Ajoute un message flash après la soumission réussie
        messages.success(request, 'Votre message a été envoyé avec succès !')
    
    return redirect('home')

def contact_success_view(request):
    pass
