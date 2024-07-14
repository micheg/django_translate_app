from django.urls import path
from .views import translate_text, list_languages

urlpatterns = [
    path('translate/', translate_text, name='translate_text'),
    path('languages/', list_languages, name='list_languages'),
]
