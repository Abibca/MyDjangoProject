from django.urls import path
from .import views

urlpatterns = [
    path('',views.fetch_profile),
    path('address/',views.fetch_address)
]
