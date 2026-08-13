import streamlit as st

from services.api import (
    create_student,
    get_students,
    update_student,
    delete_student
)


st.set_page_config(
    page_title="Student Management",
    page_icon="🎓",
    layout="wide"
)


st.title("🎓 Student Management System")

st.write("FastAPI + Supabase + Streamlit")


menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create Student",
        "View Students",
        "Update Student",
        "Delete Student"
    ]
)


# =========================
# CREATE STUDENT
# =========================

if menu == "Create Student":

    st.header("Create Student")

    name = st.text_input("Student Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone")

    course = st.text_input("Course")


    if st.button("Create Student"):

        if not name or not email:

            st.warning("Name and Email are required")

        else:

            student_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "course": course
            }

            try:

                result = create_student(student_data)

                st.success("Student created successfully!")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")


# =========================
# VIEW STUDENTS
# =========================

elif menu == "View Students":

    st.header("All Students")

    if st.button("Load Students"):

        try:

            students = get_students()

            if students:

                st.dataframe(
                    students,
                    use_container_width=True
                )

            else:

                st.info("No students found.")

        except Exception as e:

            st.error(f"Error: {e}")


# =========================
# UPDATE STUDENT
# =========================

elif menu == "Update Student":

    st.header("Update Student")

    student_id = st.text_input("Student ID")

    name = st.text_input("New Name")

    email = st.text_input("New Email")

    phone = st.text_input("New Phone")

    course = st.text_input("New Course")


    if st.button("Update Student"):

        if not student_id:

            st.warning("Student ID is required")

        else:

            student_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "course": course
            }

            try:

                result = update_student(
                    student_id,
                    student_data
                )

                st.success("Student updated successfully!")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")


# =========================
# DELETE STUDENT
# =========================

elif menu == "Delete Student":

    st.header("Delete Student")

    student_id = st.text_input("Student ID")


    if st.button("Delete Student"):

        if not student_id:

            st.warning("Student ID is required")

        else:

            try:

                result = delete_student(student_id)

                st.success("Student deleted successfully!")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")