from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from webapp.views import (
    book_with_friends,
    booking,
    booking_pk,
    hall,
    hall_pk,
    movies,
    movies_pk,
    seats,
    seats_pk,
    showtime,
    showtime_pk,
    theater,
    theater_pk,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Dummy API",
        default_version="v1",
        description="Dummy description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "playground/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/movies", movies),
    path("api/movies/<int:pk>", movies_pk),
    path("api/theater", theater),
    path("api/theater/<int:pk>", theater_pk),
    path("api/hall", hall),
    path("api/hall/<int:pk>", hall_pk),
    path("api/showtime", showtime),
    path("api/showtime/<int:pk>", showtime_pk),
    path("api/seats", seats),
    path("api/seats/<int:pk>", seats_pk),
    path("api/bookingDetails", booking),
    path("api/bookingDetails/<int:pk>", booking_pk),
    path("api/book_with_friends", book_with_friends),
]
