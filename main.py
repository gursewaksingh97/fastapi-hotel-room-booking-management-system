from fastapi import FastAPI,status,HTTPException,Depends,Request
from database import engine,SessionLocal,get_db
from models import Base,HotelBooking
from schemas import HotelBooking as HotelBookingSchema    #Pydentic Schemas
from schemas import UpdateBooking    #Pydentic Schemas
from schemas import ResponseBooking      #response Schemas

import time

app=FastAPI()
Base.metadata.create_all(bind=engine)

# Middleware
@app.middleware("http")
async def log_time(request:Request,call_next):
    start_time=time.time()
    print("Request Method:",request.method)
    print("Request URL:",request.url)
    response = await call_next(request)
    end_time=time.time()
    process_time=end_time-start_time
    print(f"Request Processing Time: {process_time}")
    return response


@app.get("/")
def home():
    return {'message': "Welcome To Hotel Booking Management System "}

# View Bookings
@app.get("/bookings",response_model=list[ResponseBooking])
def get_bookings(db=Depends(get_db)):
    bookings=db.query(HotelBooking).all()
    if bookings is None :
        raise HTTPException(status_code=404,detail="Booking List Is Empty...")
    return bookings

# Search Specific Booking 
@app.get("/bookings/{booking_id}",response_model=ResponseBooking)
def get_booking(booking_id:int,db=Depends(get_db)):
    booking=db.query(HotelBooking).filter(HotelBooking.booking_id==booking_id).first()
    if booking is None :
        raise HTTPException(status_code=404,detail="Booking Not Found...... ")
    return booking

# Add Booking 
@app.post("/bookings/add_booking",response_model=ResponseBooking,status_code=status.HTTP_201_CREATED)
def add_booking(emp:HotelBookingSchema,db=Depends(get_db)):
    existing_booking=db.query(HotelBooking).filter(HotelBooking.booking_id==emp.booking_id).first()
    if existing_booking is not None:
        raise HTTPException(status_code=400,detail="Booking Already Exists...")
    else:
        booking=HotelBooking(booking_id=emp.booking_id,customer_name=emp.customer_name,room_type=emp.room_type,number_of_days=emp.number_of_days)
        db.add(booking)
        db.commit()
        return booking

# Update Booking 
@app.put("/bookings/updatebooking/{booking_id}")
def update_booking(booking_id:int,emp:UpdateBooking,db=Depends(get_db)):
    booking=db.query(HotelBooking).filter(HotelBooking.booking_id==booking_id).first()
    if booking is None :
        raise HTTPException(status_code=404,detail="Booking Not Found...... ")
    else:
        booking.room_type= emp.room_type
        booking.number_of_days=emp.number_of_days
        db.commit()
        return {'message':"Booking details Updated Successful....."}

# Delete Booking 
@app.delete("/bookings/delete_booking/{booking_id}")
def delete_booking(booking_id:int,db=Depends(get_db),):
    booking=db.query(HotelBooking).filter(HotelBooking.booking_id==booking_id).first()
    if booking is None :
        raise HTTPException(status_code=404,detail="Booking Not Found...... ")
    else:
        db.delete(booking)
        db.commit()
        return {'Message':"Booking Deleted Successfully"}



