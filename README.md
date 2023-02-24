# Movie Ticket Booking API- Django REST framework (DRF)

This is a project that provides APIs for a movie theater booking system. The APIs can be used to perform CRUD operations about movies, theaters, halls, showtimes, seats, and booking details. It also provides an endpoint to book tickets with friends. It keeps in mind the constraints to have alteast 6 seats per row and maintain unique instances.

## Additional Features
- API Documentation at http://localhost:8000/docs/ or you can play around at http://localhost:8000/playground/
- Sends Email to recepient whenever a error occurs.
- Used pre-commit for best coding standards.
- Provided a elaborate ERD diagram to better understand the database.
- Modified admin file therefore you can manage data more intuitively admin panel.

## Getting Started

To get started with the project, you can follow these steps for a LINUX-UBUNTU system:

1. Clone the repository: `git clone https://github.com/amanrOnly/Movie_ticket_booking.git`
2. Create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment: `source env/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Run the migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Access the admin panel at 'http://localhost:8000/admin'
8. If default Username and Password both "qwe" doesn't work, in bash run 'python manage.py createsuperuser' and create your own Username and Password. 

The application will be accessible at `http://localhost:8000/`

The APIs follow a similar structure where an endpoint without a primary key supports GET and POST requests, while an endpoint with a primary key supports GET, PUT and DELETE requests.

## ERD Diagram
The ERD (Entity Relationship Diagram) for the database used in this project is shown below:

![ERD Diagram](/api_models.png)

## APIs
The following APIs are provided:

- admin/: Django admin panel.
- api/movies: API to list or create movies.
- api/movies/<primary_key>: API to get, update or delete a specific movie.
- api/theater: API to list or create theaters.
- api/theater/<primary_key>: API to get, update or delete a specific theater.
- api/hall: API to list or create halls.
- api/hall/<primary_key>: API to get, update or delete a specific hall.
- api/showtime: API to list or create showtimes.
- api/showtime/<primary_key>: API to get, update or delete a specific showtime.
- api/seats: API to list or create seats.
- api/seats/<primary_key>: API to get, update or delete a specific seat.
- api/bookingDetails: API to list or create booking details.
- api/bookingDetails/<primary_key>: API to get, update or delete a specific booking detail.
- api/book_with_friends: API to book tickets with friends.

## API Playground

![Screenshot](/ss.png)
