"""nice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sun import views
urlpatterns = [
 
    path("",views.index,name="index"),
    path("Aries",views.Aries,name="Aries"),
    path("Taurus",views.Taurus,name="Taurus"),
    path("Gemini",views.Gemini,name="Gemini"),
    path("Cancer",views.Cancer,name="Cancer"),
    path("Leo",views.Leo,name="Leo"),
    path("Virgo",views.Virgo,name="Virgo"),
    path("Libra",views.Libra,name="Libra") , 
    path("Scorpio",views.Scorpio,name="Scorpio"),
    path("Sagitarius",views.Sagitarius,name="Sagitarius"),
    path("Capricorn",views.Capricorn,name="Capricorn"),
    path("Aquarius",views.Aquarius,name="Aquarius"),
    path("Pisces",views.Pisces,name="Pisces"),
]