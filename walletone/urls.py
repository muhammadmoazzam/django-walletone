from django.urls import path
from . import views

urlpatterns = [
    path('confirm/', views.payment_confirm, name='w1-payment-confirm'),
]
