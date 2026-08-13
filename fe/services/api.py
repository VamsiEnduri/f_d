import requests

BACKEND_URL = "https://f-d-i74a.onrender.com"

def create_student(student_data):

    response = requests.post(
        f"{BACKEND_URL}/students",
        json=student_data
    )

    response.raise_for_status()

    return response.json()


def get_students():

    response = requests.get(
        f"{BACKEND_URL}/students"
    )

    response.raise_for_status()

    return response.json()["data"]


def get_student(student_id):

    response = requests.get(
        f"{BACKEND_URL}/students/{student_id}"
    )

    response.raise_for_status()

    return response.json()


def update_student(student_id, student_data):

    response = requests.put(
        f"{BACKEND_URL}/students/{student_id}",
        json=student_data
    )

    response.raise_for_status()

    return response.json()


def delete_student(student_id):

    response = requests.delete(
        f"{BACKEND_URL}/students/{student_id}"
    )

    response.raise_for_status()

    return response.json()