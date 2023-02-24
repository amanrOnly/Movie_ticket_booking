from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='movies')
    trailer_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Hall(models.Model):
    name = models.CharField(max_length=255)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='halls')
    rows = models.PositiveIntegerField()
    column = models.PositiveIntegerField(validators=[MinValueValidator(6)])

    def __str__(self):
        return f"{self.theater} - {self.name}"
    
    def create_seats(self):
        for row in range(1, self.rows+1):
            for col in range(1, self.column+1):
                seat = Seat(hall=self, row=row, column=col)
                seat.save()

class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('hall', 'row', 'column')

    def __str__(self):
        return f"{self.hall} - Row {self.row}, Seat {self.column}"

class Showtime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='showtimes')

    def __str__(self):
        return f"{self.movie} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat, related_name='bookings')
    transaction_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('showtime', 'user')

    def __str__(self):
        return f"{self.user} - {self.showtime}"

    def update_seat_availability(self):
        for seat in self.seats.all():
            seat.available = False
            seat.save()
