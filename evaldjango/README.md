# EvalDjango — Skills Shop

Application web Django permettant à des utilisateurs d'échanger des compétences entre eux : un utilisateur propose une compétence, crée une demande (_Query_) pour une activité et un créneau donné, et un autre utilisateur possédant cette compétence peut réserver la demande pour l'aider.

## Fonctionnalités

- Inscription / connexion (basées sur `django.contrib.auth`), avec sélection des compétences possédées lors de l'inscription.
- Affichage de la liste des compétences disponibles (visiteurs et utilisateurs connectés).
- Création d'une demande (_Query_) : activité, compétence requise, créneau (date/heure).
- Consultation des créneaux disponibles pour une compétence donnée.
- Réservation d'une demande par un autre utilisateur possédant la compétence requise (impossible de réserver sa propre demande, ni sans posséder la compétence).
- Tableau de bord sur la page d'accueil listant, pour l'utilisateur connecté :
  - les demandes qu'il peut aider à satisfaire (_available_queries_),
  - les demandes qu'il a acceptées (_accepted_queries_).

## Stack technique

- Python 3.13
- Django 6.0
- Base de données SQLite (`db.sqlite3`)
- Vérification de types avec `mypy` + `django-stubs` (voir [mypy.ini](../mypy.ini))

## Structure du projet

```text
evaldjango/
├── evaldjango/         # Configuration du projet (settings, urls, wsgi/asgi)
└── skills_shop/        # Application principale
    ├── models.py        # User, Skill, Query
    ├── views.py         # index, signup, creer_demande, select_skill, book_query
    ├── forms.py         # QueryForm, SignupForm
    ├── urls.py
    ├── admin.py
    ├── templates/
    └── static/
```

## Modèles principaux

- **Skill** : une compétence (nom), reliée en `ManyToMany` aux utilisateurs qui la possèdent.
- **Query** : une demande d'aide, composée d'une activité, d'une compétence requise, d'un créneau (`slot`), de l'utilisateur demandeur (`user`) et de l'utilisateur qui l'a acceptée (`accepted_by`). La propriété `is_accepted` indique si la demande a déjà été prise en charge.

## Installation

Prérequis : Python 3.13 et Django 6.

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install django

cd evaldjango
python manage.py migrate
python manage.py createsuperuser   # optionnel, pour accéder à /admin/
python manage.py runserver
```

L'application est ensuite accessible sur `http://127.0.0.1:8000/`.

## Routes principales

| URL                       | Vue             | Description                                            |
| ------------------------- | --------------- | ------------------------------------------------------ |
| `/`                       | `index`         | Page d'accueil : liste des compétences et des demandes |
| `/signup/`                | `signup`        | Inscription                                            |
| `/accounts/...`           | Django auth     | Connexion / déconnexion                                |
| `/demande/creer/`         | `creer_demande` | Création d'une demande (connecté)                      |
| `/skill/<skill_name>/`    | `select_skill`  | Créneaux disponibles pour une compétence               |
| `/query/<query_id>/book/` | `book_query`    | Réservation d'une demande (connecté)                   |
| `/admin/`                 | Django admin    | Administration (Skill, Query)                          |

## Diagrammes

Des diagrammes PlantUML décrivant les cas d'utilisation et les classes du projet sont disponibles à la racine du dépôt : [usecase.puml](../usecase.puml) et [class-diagram.puml](../class-diagram.puml).

## Difficultés rencontrées

La gestion de la base de données a pu être compliquée par moments notamment concernant la table many to many (besoin de réflexion là-dessus).

L'algorithmie pure peut me prendre beaucoup de temps et donc je m'aide de l'IA pour me générer du code que je relie entièrement pour comprendre et ainsi valider ou non.
J'ai pu gagner beaucoup de temps en procédant de cette manière.
Le plus compliquer a été de faire le lien entre les différentes tables et donc les requêtes nécessaires pour faire le lien entre les différents modèles.

J'ai bien compris l'ensemble de l'architecture de mon projet Django.
