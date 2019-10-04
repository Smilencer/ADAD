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
    path(r'en/index/', views.index),
    path(r'zh/index/', views.index),
    path(r'en/ajax/', views.handleRequest),
    path(r'zh/ajax/', views.handleRequest),
    path(r'en/patient/', views.patient),
    path(r'zh/patient/', views.patient),
    path(r'en/symptom/', views.symptom),
    path(r'zh/symptom/', views.symptom),
    path(r'en/menu/', views.menu),
    path(r'zh/menu/', views.menu),
    path(r'en/mri/', views.mri),
    path(r'zh/mri/', views.mri),
    path(r'en/report/', views.report),
    path(r'zh/report/', views.report),
    path(r'en/indice/', views.indice),
    path(r'zh/indice/', views.indice),
    path(r'en/indice2/', views.indice2),
    path(r'zh/indice2/', views.indice2),
    path(r'en/help_diagnosis_AD_imgs/', views.help_diagnosis_AD_imgs),
    path(r'zh/help_diagnosis_AD_imgs/', views.help_diagnosis_AD_imgs),
    path(r'en/help_diagnosis_AD_text/', views.help_diagnosis_AD_text),
    path(r'zh/help_diagnosis_AD_text/', views.help_diagnosis_AD_text),
    path(r'en/help_diagnosis_AD_index/', views.help_diagnosis_AD_index),
    path(r'zh/help_diagnosis_AD_index/', views.help_diagnosis_AD_index),
    path(r'en/help_predict_AD_index/', views.help_predict_AD_index),
    path(r'zh/help_predict_AD_index/', views.help_predict_AD_index),
    path(r'en/moca/', views.moca),
    path(r'zh/moca/', views.moca),
]
