from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def put_users_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Users)
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    id: int = raw_data.id
    user_id: int = raw_data.user_id
    appointment_date: datetime.date = raw_data.appointment_date
    appointment_time: str = raw_data.appointment_time
    purpose: str = raw_data.purpose

    record_to_be_added = {
        "id": id,
        "purpose": purpose,
        "user_id": user_id,
        "appointment_date": appointment_date,
        "appointment_time": appointment_time,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_id(
    db: Session,
    id: int,
    user_id: int,
    appointment_date: str,
    appointment_time: str,
    purpose: str,
):

    query = db.query(models.Appointments)
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "id": id,
            "purpose": purpose,
            "user_id": user_id,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res


async def get_calendar_integration(db: Session):

    query = db.query(models.CalendarIntegration)

    calendar_integration_all = query.all()
    calendar_integration_all = (
        [new_data.to_dict() for new_data in calendar_integration_all]
        if calendar_integration_all
        else calendar_integration_all
    )
    res = {
        "calendar_integration_all": calendar_integration_all,
    }
    return res


async def get_calendar_integration_id(db: Session, id: int):

    query = db.query(models.CalendarIntegration)

    calendar_integration_one = query.first()

    calendar_integration_one = (
        (
            calendar_integration_one.to_dict()
            if hasattr(calendar_integration_one, "to_dict")
            else vars(calendar_integration_one)
        )
        if calendar_integration_one
        else calendar_integration_one
    )

    res = {
        "calendar_integration_one": calendar_integration_one,
    }
    return res


async def post_calendar_integration(
    db: Session, raw_data: schemas.PostCalendarIntegration
):
    id: int = raw_data.id
    appointment_id: int = raw_data.appointment_id
    calendar_details: str = raw_data.calendar_details

    record_to_be_added = {
        "id": id,
        "appointment_id": appointment_id,
        "calendar_details": calendar_details,
    }
    new_calendar_integration = models.CalendarIntegration(**record_to_be_added)
    db.add(new_calendar_integration)
    db.commit()
    db.refresh(new_calendar_integration)
    calendar_integration_inserted_record = new_calendar_integration.to_dict()

    res = {
        "calendar_integration_inserted_record": calendar_integration_inserted_record,
    }
    return res


async def put_calendar_integration_id(
    db: Session, id: int, appointment_id: int, calendar_details: str
):

    query = db.query(models.CalendarIntegration)
    calendar_integration_edited_record = query.first()

    if calendar_integration_edited_record:
        for key, value in {
            "id": id,
            "appointment_id": appointment_id,
            "calendar_details": calendar_details,
        }.items():
            setattr(calendar_integration_edited_record, key, value)

        db.commit()
        db.refresh(calendar_integration_edited_record)

        calendar_integration_edited_record = (
            calendar_integration_edited_record.to_dict()
            if hasattr(calendar_integration_edited_record, "to_dict")
            else vars(calendar_integration_edited_record)
        )
    res = {
        "calendar_integration_edited_record": calendar_integration_edited_record,
    }
    return res


async def delete_calendar_integration_id(db: Session, id: int):

    query = db.query(models.CalendarIntegration)

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        calendar_integration_deleted = record_to_delete.to_dict()
    else:
        calendar_integration_deleted = record_to_delete
    res = {
        "calendar_integration_deleted": calendar_integration_deleted,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    query = db.query(models.Users)

    creorts = query.all()
    creorts = [new_data.to_dict() for new_data in creorts] if creorts else creorts

    # dfasfa
    if id != id:

        query = db.query(models.CalendarIntegration)

        desksd = query.all()
        desksd = [new_data.to_dict() for new_data in desksd] if desksd else desksd
    else:

        query = db.query(models.Appointments)

        condosksd = query.all()
        condosksd = (
            [new_data.to_dict() for new_data in condosksd] if condosksd else condosksd
        )

        raise HTTPException(status_code=200, detail=" Message decoraror")
    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res
