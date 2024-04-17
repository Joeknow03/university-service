import pytest
from app.api.models import UniversityIn, UniversityOut

universities = UniversityIn(
    name='Mirea',
    phone='+791234567',
    city='Moscow',
    count_students=20000
)


def test_create_reader(universities: UniversityIn = universities):
    assert dict(universities) == {'name': universities.name,
                                  'phone': universities.phone,
                                  'city': universities.city,
                                  'count_students': universities.count_students
                                  }


def test_update_reader_age(universities: UniversityIn = universities):
    university_upd = UniversityOut(
        name='Mirea',
        phone='+791234567',
        city='Moscow',
        count_students=20000,
        id=1
    )
    assert dict(university_upd) == {'name': universities.name,
                                'phone': universities.phone,
                                'city': universities.city,
                                'count_students': universities.count_students,
                                'id': university_upd.id
                                }


def test_update_reader_city(universities: UniversityIn = universities):
    university_upd = UniversityIn(
        name=universities.name,
        phone=universities.phone,
        city=universities.city,
        count_students=universities.count_students,
        id=1
    )
    assert dict(university_upd) == {'name': universities.name,
                                'phone': universities.phone,
                                'city': universities.city,
                                'count_students': universities.count_students,
                                'id': university_upd.id
                                }
