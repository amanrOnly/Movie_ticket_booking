from django.contrib import admin
# from django.apps import apps
from .models import Theater, Movie, Hall, Seat, Showtime, Booking

# for model in apps.get_models():
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Showtime)