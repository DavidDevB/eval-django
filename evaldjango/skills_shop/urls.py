from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('demande/creer/', views.creer_demande, name='creer_demande'),
    path('skill/<str:skill_name>/', views.select_skill, name='select_skill'),
    path('slot/<int:slot_id>/book/', views.book_slot, name='book_slot'),
    path('signup/', views.signup, name='signup'),
]