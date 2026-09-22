from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('demande/creer/', views.creer_demande, name='creer_demande'),
    path('skill/<str:skill_name>/', views.select_skill, name='select_skill'),
    path('query/<int:query_id>/book/', views.book_query, name='book_query'),
    path('signup/', views.signup, name='signup'),
    
]