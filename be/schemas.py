from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):

    name: str

    email: EmailStr

    phone: str | None = None

    course: str | None = None

class StudentUpdate(BaseModel):

    name: str | None = None

    email: EmailStr | None = None

    phone: str | None = None

    course: str | None = None    