from pydantic import BaseModel
from typing import List, Optional

class UniversityIn(BaseModel):
    name: str
    phone: str
    city: str
    count_students: int

class UniversityOut(UniversityIn):
    id: int
