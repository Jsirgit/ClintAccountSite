# accounts/urls.py

from django.urls import path
from acap import views  
# home_view

urlpatterns = [
     path('', views.hm, name='hm'),
    path('clients_list/', views.clients_list, name='clients_list'),
    path('invoices/', views.invoices_list, name='invoices_list'),
    # path('', home_view, name='home'),
]
