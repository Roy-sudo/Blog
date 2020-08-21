from django.urls import path
from .views import BookingView, BookingDetailView

urlpatterns = [
    path('', BookingView.as_view(), name="bookings"),
    path('bookings/<int:pk>', BookingDetailView.as_view(), name="bookings-details"),
]
