from pydantic import BaseModel

# Pydentic Model - Post
class HotelBooking(BaseModel):
    booking_id:int
    customer_name:str
    room_type:str
    number_of_days:int


# Pydentic Model - Put
class UpdateBooking(BaseModel):
    room_type:str
    number_of_days:int


# Response Model 
class ResponseBooking(BaseModel):
    booking_id:int
    room_type:str
    number_of_days:int
