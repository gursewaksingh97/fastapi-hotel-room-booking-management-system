
from sqlalchemy import Column, Integer, String

from database import Base

class HotelBooking(Base):
    __tablename__="HotelBooking"
    booking_id=Column(Integer,primary_key=True)
    customer_name=Column(String)
    room_type=Column(String)
    number_of_days=Column(Integer)

