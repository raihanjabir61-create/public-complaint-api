# Public Complaint API

Backend API menggunakan FastAPI untuk pengelolaan pengaduan masyarakat.

## Teknologi

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Struktur

app/
├── main.py
├── routers/
├── schemas/
├── services/
└── repositories/

tests/

## Menjalankan Project

Install dependency:

pip install -r requirements.txt

Jalankan server:

uvicorn app.main:app --reload

Swagger:

http://127.0.0.1:8000/docs

## Testing

pytest