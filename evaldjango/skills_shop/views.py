from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    contexte = { 'titre_page': 'Skills shop', 'skills': ['development', 'cooking', 'writing', 'painting'], 'slots': []}
    return render(request, 'index.html', contexte)

def creer_demande(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.utilisateur = request.user  # on associe la demande à l'utilisateur connecté
            demande.save()
    return redirect('accueil')