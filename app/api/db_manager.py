from app.api.models import UniversityIn, UniversityOut
from app.api.db import universities, database


async def add_university(payload: UniversityIn):
    query = universities.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_university():
    query = universities.select()
    return await database.fetch_all(query=query)


async def get_university(id):
    query = universities.select().where(universities.c.id == id)
    return await database.fetch_one(query=query)


async def delete_university(id: int):
    query = universities.delete().where(universities.c.id == id)
    return await database.execute(query=query)

