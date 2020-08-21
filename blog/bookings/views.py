from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Booking

# def bookings(request):
#     return render(request, 'bookings.html', {})

class BookingView(ListView):
    model = Booking
    template_name = 'bookings.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'bookings_details.html'

    

