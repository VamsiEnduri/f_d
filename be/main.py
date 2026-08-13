from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db import supabase_obj

from schemas import StudentCreate, StudentUpdate


app = FastAPI(
    title="Student Management API",
    description="FastAPI + Supabase CRUD API",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "success": True,
        "message": "Student Management API is running"
    }


# =========================
# CREATE
# =========================

@app.post("/students")
def create_student(student: StudentCreate):

    try:

        response = (
            supabase_obj
            .table("students")
            .insert(student.model_dump())
            .execute()
        )

        return {
            "success": True,
            "message": "Student created successfully",
            "data": response.data
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# READ ALL
# =========================

@app.get("/students")
def get_students():

    try:

        response = (
            supabase_obj
            .table("students")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        return {
            "success": True,
            "message": "Students fetched successfully",
            "data": response.data
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# READ ONE
# =========================

@app.get("/students/{student_id}")
def get_student(student_id: str):

    try:

        response = (
            supabase_obj
            .table("students")
            .select("*")
            .eq("id", student_id)
            .execute()
        )

        if not response.data:

            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "success": True,
            "message": "Student fetched successfully",
            "data": response.data[0]
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# UPDATE
# =========================

@app.put("/students/{student_id}")
def update_student(
    student_id: str,
    student: StudentUpdate
):

    try:

        update_data = student.model_dump(
            exclude_unset=True
        )

        if not update_data:

            raise HTTPException(
                status_code=400,
                detail="No data provided"
            )

        response = (
            supabase_obj
            .table("students")
            .update(update_data)
            .eq("id", student_id)
            .execute()
        )

        if not response.data:

            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "success": True,
            "message": "Student updated successfully",
            "data": response.data
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# =========================
# DELETE
# =========================

@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    try:

        response = (
            supabase_obj
            .table("students")
            .delete()
            .eq("id", student_id)
            .execute()
        )

        if not response.data:

            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "success": True,
            "message": "Student deleted successfully",
            "data": response.data
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )