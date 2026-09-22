from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .forms import DemandeForm
from .models import Query, Skill
from django.contrib.auth.decorators import login_required


@require_http_methods(["GET"])
def index(request):
    skills = Skill.objects.all()
    contexte = { 'skills': skills, 'demandes_disponibles': [] }
    return render(request, 'index.html', contexte)

@login_required
def creer_demande(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.user = request.user
            demande.save()
    return redirect('index')

@require_http_methods(["GET"])
def select_skill(request, skill_name):
    slots = Query.objects.filter(skill__name=skill_name)
    contexte = {'skill_name': skill_name, 'slots': slots}
    return render(request, 'slots.html', contexte)

@require_http_methods(["POST"])
def book_slot(request, slot_id):
    slot = Query.objects.get(id=slot_id)
    slot.user = request.user
    slot.save()
    return redirect('index')