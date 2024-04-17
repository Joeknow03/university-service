from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import UniversityIn, UniversityOut
from app.api import db_manager

universities = APIRouter()

@universities.post('/', response_model=UniversityOut, status_code=201)
async def create_university(payload: UniversityIn):
    university_id = await db_manager.add_university(payload)

    response = {
        'id':university_id,
        **payload.dict()
    }

    return response


@universities.get('/', response_model=List[UniversityOut])
async def get_universities():
    return await db_manager.get_all_university()


@universities.get('/{id}/', response_model=UniversityOut)
async def get_university(id: int):
    university = await db_manager.get_university(id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return university


@universities.delete('/{id}/', response_model=None)
async def delete_university(id: int):
    university = await db_manager.get_university(id)
    if not university:
        raise HTTPException(status_code=404, detail="University not found")
    return await db_manager.delete_university(id)