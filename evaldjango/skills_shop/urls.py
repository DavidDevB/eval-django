from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('demande/creer/', views.creer_demande, name='creer_demande'),
]