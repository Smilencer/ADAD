"""ADAD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from myAPP import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'index/', views.index),
    path(r'ajax/', views.handleRequest),
    path(r'patient/', views.patient),
    path(r'symptom/', views.symptom),
    path(r'menu/', views.menu),
    path(r'mri/', views.mri),
    path(r'report/', views.report),
    path(r'indice/', views.indice),
    path(r'indice2/', views.indice2),
    path(r'help_diagnosis_AD_imgs/', views.help_diagnosis_AD_imgs),
    path(r'help_diagnosis_AD_text/', views.help_diagnosis_AD_text),
    path(r'help_diagnosis_AD_index/', views.help_diagnosis_AD_index),
    path(r'help_predict_AD_index/', views.help_predict_AD_index),
    path(r'moca/', views.moca),
]
