from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    user_id: int
    appointment_date: datetime.date
    appointment_time: Any
    purpose: str


class ReadAppointments(BaseModel):
    id: Any
    user_id: int
    appointment_date: datetime.date
    appointment_time: Any
    purpose: str
    class Config:
        from_attributes = True


class CalendarIntegration(BaseModel):
    id: Any
    appointment_id: int
    calendar_details: str


class ReadCalendarIntegration(BaseModel):
    id: Any
    appointment_id: int
    calendar_details: str
    class Config:
        from_attributes = True




class PostAppointments(BaseModel):
    id: int = Field(...)
    user_id: int = Field(...)
    appointment_date: Any = Field(...)
    appointment_time: str = Field(..., max_length=100)
    purpose: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostCalendarIntegration(BaseModel):
    id: int = Field(...)
    appointment_id: int = Field(...)
    calendar_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

