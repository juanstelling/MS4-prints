from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company, name='company'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('faq/', views.faq, name='faq'),
    path('return-policy/', views.return_policy, name='return_policy'),
]
