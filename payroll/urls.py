from django.urls import path
from . import views

urlpatterns = [
  path("input", views.Inputs),
  path('trial', views.Trial),
  path("payroll", views.Payroll)
]