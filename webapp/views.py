from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Theater, Hall, Showtime, Seat, Booking
from .serializers import MovieSerializer, TheaterSerializer, HallSerializer, ShowSerializer, SeatSerializer, BookingSerializer
from .email import send_email_on_error

#-----------------------------------MOVIE-------------------------------------
#  API without PRIMARY KEY

@send_email_on_error
@api_view(['GET' , 'POST'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#  API With PRIMARY KEY
@send_email_on_error
@api_view(['DELETE' , 'GET' , 'PUT'])
def movies_pk(request , pk):

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#-----------------------------------THEATER-------------------------------------

#  API WITHOUT PRIMARY KEY
@send_email_on_error
@api_view(['GET' , 'POST'])
def theater(request):
    if request.method == 'GET':
        theaters = Theater.objects.all()
        serializer = TheaterSerializer(theaters, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TheaterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#  API With PRIMARY KEY

@send_email_on_error
@api_view(['DELETE' , 'GET' , 'PUT'])
def theater_pk(request , pk):

    try:
        theaters = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        theaters.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = TheaterSerializer(theaters)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TheaterSerializer(theaters , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#-----------------------------------HALL-------------------------------------

#  API WITHOUT PRIMARY KEY

@send_email_on_error
@api_view(['GET' , 'POST'])
def hall(request):
    if request.method == 'GET':
        halls = Hall.objects.all()
        serializer = HallSerializer(halls, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HallSerializer(data = request.data)
        if serializer.is_valid():
            hall = serializer.save()
            hall.create_seats()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#  API with PRIMARY KEY

@send_email_on_error
@api_view(['DELETE' , 'GET'])
def hall_pk(request , pk):

    try:
        halls = Hall.objects.get(pk=pk)
    except Hall.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        halls.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = HallSerializer(halls)
        return Response(serializer.data)

#-----------------------------------SHOWTIME-------------------------------------

#  API WITHOUT PRIMARY KEY

@api_view(['GET' , 'POST'])
def showtime(request):
    if request.method == 'GET':
        shows = Showtime.objects.all()
        serializer = ShowSerializer(shows, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ShowSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#  API with PRIMARY KEY

@send_email_on_error
@api_view(['DELETE' , 'GET' , 'PUT'])
def showtime_pk(request , pk):

    try:
        shows = Showtime.objects.get(pk=pk)
    except Showtime.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        shows.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = ShowSerializer(shows)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShowSerializer(shows , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#-----------------------------------SEATS-------------------------------------

#  API WITHOUT PRIMARY KEY

@send_email_on_error
@api_view(['GET' , 'POST'])
def seats(request):
    if request.method == 'GET':
        seat = Seat.objects.all()
        serializer = SeatSerializer(seat, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SeatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#  API PRIMARY KEY

@send_email_on_error
@api_view(['DELETE' , 'GET' , 'PUT'])
def seats_pk(request , pk):

    try:
        seat = Seat.objects.get(pk=pk)
    except Seat.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = SeatSerializer(seat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SeatSerializer(seat , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#-----------------------------------BOOKING-------------------------------------

#  API WITHOUT PRIMARY KEY

@send_email_on_error
@api_view(['GET' , 'POST'])
def booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookingSerializer(data = request.data)
        if serializer.is_valid():
            booking = serializer.save()
            booking.update_seat_availability()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#  API with PRIMARY KEY

@send_email_on_error
@api_view(['DELETE' , 'GET' , 'PUT'])
def booking_pk(request , pk):

    try:
        bookings = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        bookings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = BookingSerializer(bookings)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookingSerializer(bookings , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@send_email_on_error
@api_view(['POST'])
def book_with_friends(request):
    # Get movie, time and theater from request data
    movie_id = request.data.get('movie_id')
    showtime_id = request.data.get('showtime_id')
    theater_id = request.data.get('theater_id')

    # Get seats to be booked
    seat_ids = request.data.get('seats')
    seats = Seat.objects.filter(id__in=seat_ids)

    # Check if seats can be booked together
    rows = set([seat.row for seat in seats])
    columns = set([seat.column for seat in seats])
    if len(rows) > 1 and len(columns) > 1:  # Checking for seats are together or not
        # Suggest other showtimes
        suggestions = []
        showtimes = Showtime.objects.filter(movie_id=movie_id, hall__theater_id=theater_id).order_by('start_time')
        for showtime in showtimes:
            available_seats = showtime.hall.seats.filter(available=True)
            available_rows = set([seat.row for seat in available_seats])
            available_columns = set([seat.column for seat in available_seats])
            if rows.issubset(available_rows) and columns.issubset(available_columns):
                # Seats are available for this showtime
                suggestions.append({
                    'showtime_id': showtime.id,
                    'start_time': showtime.start_time,
                    'end_time': showtime.end_time,
                })
        return Response({'message': 'Seats are not together', 'suggestions': suggestions})

    # Book the seats
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        booking = serializer.instance
        booking.update_seat_availability()

        return Response(serializer.data)
    else:
        return Response(serializer.errors)
