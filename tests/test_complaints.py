from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_complaint():

    response = client.post(
        "/api/v1/complaints",
        json={
            "citizen_name": "Budi Santoso",
            "title": "Sampah Menumpuk",
            "description": "Sampah menumpuk di sekitar lingkungan warga.",
            "category": "kebersihan",
            "location": "Jl. Mawar"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["citizen_name"] == "Budi Santoso"
    assert data["category"] == "kebersihan"
    assert data["status"] == "diajukan"


def test_get_complaints():

    response = client.get(
        "/api/v1/complaints"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_nonexistent_complaint():

    response = client.get(
        "/api/v1/complaints/99999"
    )

    assert response.status_code == 404


def test_invalid_complaint():

    response = client.post(
        "/api/v1/complaints",
        json={
            "citizen_name": "A",
            "title": "B",
            "description": "C",
            "category": "kategori_salah",
            "location": "D"
        }
    )

    assert response.status_code == 422