# accounts/views.py

from django.shortcuts import render, HttpResponse
from .models import Client, Invoice

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients_list.html', {'clients': clients})

def invoices_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices_list.html', {'invoices': invoices})

def hm(request):
    return render(request, 'hm.html')
# def home_view(request):
#     # Sample data for demonstration purposes
#     invoices = [
#         {'client': 'Client A', 'date': '2023-08-01', 'amount': 1000},
#         {'client': 'Client B', 'date': '2023-08-02', 'amount': 1500},
#         {'client': 'Client C', 'date': '2023-08-03', 'amount': 2000},
#     ]

#     return render(request, 'home.html', {'invoices': invoices})