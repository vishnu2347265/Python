from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="homepage"),
    path('about', views.about, name="about_sdg4"),
    path('registration', views.registration, name="registration"),  
]
