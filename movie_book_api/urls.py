from django.contrib import admin
from django.urls import path
from webapp.views import movies_pk, movies, theater, theater_pk, hall, hall_pk, showtime, showtime_pk, seats_pk, seats, booking, booking_pk, book_with_friends

urlpatterns = [
    path('/', admin.site.urls),
    path('api/movies', movies),
    path('api/movies/<int:pk>', movies_pk),
    path('api/theater', theater),
    path('api/theater/<int:pk>', theater_pk),
    path('api/hall', hall),
    path('api/hall/<int:pk>', hall_pk),
    path('api/showtime', showtime),
    path('api/showtime/<int:pk>', showtime_pk),
    path('api/seats', seats),
    path('api/seats/<int:pk>', seats_pk),
    path('api/bookingDetails', booking),
    path('api/bookingDetails/<int:pk>', booking_pk),
    path('api/book_with_friends', book_with_friends)
]
