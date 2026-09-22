from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .forms import QueryForm, SignupForm
from .models import Query, Skill
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.skills.set(form.cleaned_data['skills'])
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@require_http_methods(["GET"])
def index(request):
    skills = Skill.objects.all()
    if request.user.is_authenticated:
        available_queries = Query.objects.filter(skill__in=request.user.skills.all())
        user_queries = Query.objects.filter(user=request.user)
    else:
        available_queries = []
        user_queries = []
    contexte = { 'skills': skills, 'available_queries': available_queries, 'user_queries': user_queries }
    return render(request, 'index.html', contexte)

@login_required
def creer_demande(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.user = request.user
            query.save()
    return redirect('index')

@require_http_methods(["GET"])
def select_skill(request, skill_name):
    queries = Query.objects.filter(skill__name=skill_name)
    contexte = {'skill_name': skill_name, 'queries': queries}
    return render(request, 'slots.html', contexte)

@login_required
@require_http_methods(["POST"])
def book_query(request, query_id):
    query = Query.objects.get(id=query_id)
    query.accepted_by = request.user
    query.save()
    return redirect('index')