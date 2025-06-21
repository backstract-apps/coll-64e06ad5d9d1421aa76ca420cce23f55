from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/id')
async def get_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/id/')
async def put_appointments_id(id: int, user_id: int, appointment_date: str, appointment_time: Annotated[str, Query(max_length=100)], purpose: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_id(db, id, user_id, appointment_date, appointment_time, purpose)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/id')
async def delete_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_integration/')
async def get_calendar_integration(db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_integration(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/calendar_integration/id')
async def get_calendar_integration_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_calendar_integration_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/calendar_integration/')
async def post_calendar_integration(raw_data: schemas.PostCalendarIntegration, db: Session = Depends(get_db)):
    try:
        return await service.post_calendar_integration(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/calendar_integration/id/')
async def put_calendar_integration_id(id: int, appointment_id: int, calendar_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_calendar_integration_id(db, id, appointment_id, calendar_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/calendar_integration/id')
async def delete_calendar_integration_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_calendar_integration_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

