# 🎬 Movie Ticket Booking System – Django REST Framework

A fully functional backend API for booking movie tickets.  
Includes user authentication (JWT), movie & show listings, seat booking, booking history, and Swagger documentation.

---

## 🚀 Features
- User Signup & JWT Login  
- List Movies  
- List Shows for each Movie  
- Book a Seat (with validation)  
- Prevent double booking  
- Cancel a Booking  
- View My Bookings  
- Protected routes using JWT  
- Swagger API Documentation  

---

## 📦 Tech Stack
- Django  
- Django REST Framework  
- SimpleJWT  
- drf-yasg (Swagger UI)  
- SQLite (default)  

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
git clone [https://github.com/Nasir-Uddin-Mollah/Movie-Ticket-Booking-System]
cd movie_ticket_booking_system


### 2️⃣ Create & Activate Virtual Environment
On Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Apply Migrations
python manage.py migrate

### 5️⃣ Run the Development Server
python manage.py runserver

Your API is now live at:
👉 http://127.0.0.1:8000/


## 🔐 Authentication (JWT)
This project uses SimpleJWT for authentication.

### 1️⃣ Signup
POST /users/signup/
Example:
{
  "username": "risan",
  "password": "abcd1234%",
  "confirm_password": "abcd1234%"
}

### 2️⃣ Login (Get JWT Tokens)
POST /login/
Response:
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}

### 3️⃣ Authenticated Requests
Send the Access token in the header:
Authorization: Bearer <your_access_token>
Example:
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....


## 🎬 Available API Endpoints
Movies
GET ->	/movies/	List all movies

Shows
GET	->  /movies/<movie_id>/shows/	List shows for a movie
POST ->	/shows/<show_id>/book/	Book seat for a show

Bookings
GET ->	/bookings/my_bookings/	List bookings of logged-in user
POST ->	/bookings/<id>/cancel/	Cancel a booking

Booking Example:
POST /shows/3/book/
Headers:
Content-Type: application/json
Authorization: Bearer <your_access_token>
Body:
{
  "seat_number": 12
}

## 📄 Swagger Documentation
Swagger UI is available at:
👉 http://127.0.0.1:8000/swagger/
You can test APIs directly from there.
JWT input fields will appear under Authorize 🔒.


## ✔️ Extra Notes
- Prevents double booking
- Cancelling booking frees the seat
- Uses permission classes for secure routes
- Clean ViewSets with action decorators
- Easy to scale