# Movie_ticket_booking

This is a project that provides APIs for a movie theater booking system. The APIs can be used to get information about movies, theaters, halls, showtimes, seats, and booking details. It also provides an endpoint to book tickets with friends.

## Features
- API Documentation at http://localhost:8000/docs/ it you want to play around go to http://localhost:8000/playground/
![Screenshot](/ss.png)
- It has CRUD operations for tables: movies, theater, hall, showtime, seats, booking details
- Also, a POST API to book tickets with friend
- It's made such that in a row there should be atleast 6 seats and with unique bookings.
- Sends Email to recepient whenever a error occurs.
- Used pre-commit to meet coding standards
- Provided a elaborate ERD diagram to better understand the database.
- Modified admin panel therefore you can manage data more intuitively.

##APIs
The following APIs are provided:

-admin/: Django admin panel.
-api/movies: API to list or create movies.
-api/movies/<primary_key>: API to get, update or delete a specific movie.
-api/theater: API to list or create theaters.
-api/theater/<primary_key>: API to get, update or delete a specific theater.
-api/hall: API to list or create halls.
-api/hall/<primary_key>: API to get, update or delete a specific hall.
-api/showtime: API to list or create showtimes.
-api/showtime/<primary_key>: API to get, update or delete a specific showtime.
-api/seats: API to list or create seats.
-api/seats/<primary_key>: API to get, update or delete a specific seat.
-api/bookingDetails: API to list or create booking details.
-api/bookingDetails/<primary_key>: API to get, update or delete a specific booking detail.
-api/book_with_friends: API to book tickets with friends.

The APIs follow a similar structure where an endpoint without a primary key supports GET and POST requests, while an endpoint with a primary key supports GET, PUT and DELETE requests.

##ERD Diagram
The ERD (Entity Relationship Diagram) for the database used in this project is shown below:

![ERD Diagram](/api_models.png)


Documentation and Getting Started
The API documentation can be accessed at the /docs/ endpoint of the application. It provides detailed information about the APIs, their parameters, and their responses.

To get started with the project, you can follow these steps:

Clone the repository: git clone https://github.com/your-username/your-repo.git
Create a virtual environment: python3 -m venv env
Activate the virtual environment: source env/bin/activate
Install the dependencies: pip install -r requirements.txt
Run the migrations: python manage.py migrate
Start the server: python manage.py runserver
The application will be accessible at http://localhost:8000/. You can use the API endpoints described above to interact with the application.
