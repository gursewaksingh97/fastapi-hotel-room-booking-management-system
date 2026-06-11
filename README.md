🏨 Hotel Room Booking Management System

A backend CRUD application developed using FastAPI, PostgreSQL, SQLAlchemy ORM, and Pydantic for managing hotel room bookings and customer reservations.

The project demonstrates modern backend development concepts including API development, database integration, response models, exception handling, dependency injection, middleware, and proper status code implementation.

⸻

🚀 Features

* Create Hotel Bookings
* Retrieve Booking Records
* Update Room Details
* Delete Booking Records
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Pydantic Request Validation
* Response Models
* HTTP Status Codes
* Exception Handling
* Dependency Injection
* Middleware Logging
* Swagger UI Documentation

⸻

🛠️ Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic
* Uvicorn
* Postman


⸻

🗄️ Database Schema

Table: HotelBooking

Column Name	Data Type
booking_id	Integer
customer_name	String
room_type	String
number_of_days	Integer

⸻

📌 API Endpoints

Create Booking

POST /add_booking

Get All Bookings

GET /bookings

Update Booking

PUT /bookings/updatebooking/{booking_id}/{new_room_type}/{new_number_of_days}

Delete Booking

DELETE /bookings/delete_booking/{booking_id}

⸻

⚙️ Advanced Concepts Implemented

Pydantic Models

Used for request validation and structured data handling.

Response Models

Implemented standardized API responses.

Status Codes

Proper HTTP status codes used for API responses.

Exception Handling

Handled scenarios such as:

* Booking Not Found
* Duplicate Booking ID

Dependency Injection

Implemented using:

Depends(get_db)

for database session management.

Middleware

Custom middleware implemented to log:

* Request Method
* Request URL
* Processing Time

⸻

🔄 Project Workflow

User

⬇

Swagger UI / Postman

⬇

Pydantic Validation

⬇

FastAPI Endpoints

⬇

Exception Handling

⬇

Dependency Injection

⬇

SQLAlchemy ORM

⬇

PostgreSQL Database

⬇

Middleware Logging

⸻

📸 Project Documentation

This repository also includes:

* Project Description Document
* Step-by-Step Implementation Guide
* Interactive HTML Documentation Website
* API Testing Screenshots
* Database Screenshots

⸻

🎯 Learning Outcomes

Through this project I gained practical experience with:

* Backend API Development
* FastAPI Framework
* PostgreSQL Integration
* SQLAlchemy ORM
* API Testing with Postman
* Exception Handling
* Dependency Injection
* Middleware Implementation
* Database Driven Applications

⸻

👨‍💻 Author

Gursewak Singh

Aspiring Data Analyst & Python Developer

Skilled in Python, SQL, Power BI, FastAPI, Streamlit, PostgreSQL and Data Analytics.
