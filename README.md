# Public Complaint API

## Deskripsi Proyek

**Public Complaint API** adalah backend REST API yang dikembangkan menggunakan **FastAPI dan Python** untuk mengelola pengaduan masyarakat.

API ini dirancang sebagai bagian dari tugas mata kuliah **Pemrograman Lanjut** dengan menerapkan beberapa konsep utama pengembangan backend, yaitu:

1. **Modular Architecture**
2. **Data Contract menggunakan Pydantic**
3. **Unit Testing menggunakan Pytest**
4. **Version Control menggunakan Git**

Sistem ini menyediakan API untuk membuat, melihat, memperbarui status, dan menghapus data pengaduan masyarakat.

---

## Tujuan

Proyek ini bertujuan untuk:

- Menerapkan pembuatan REST API menggunakan FastAPI.
- Menerapkan struktur project yang modular.
- Menerapkan validasi dan kontrak data menggunakan Pydantic.
- Membuat endpoint CRUD untuk data pengaduan masyarakat.
- Mengimplementasikan unit test untuk memastikan fungsi API berjalan dengan baik.
- Menggunakan Git sebagai version control dan melakukan deployment source code ke repository GitHub.

---

## Fitur Utama

Public Complaint API memiliki beberapa fitur utama:

- Membuat pengaduan masyarakat.
- Menampilkan seluruh pengaduan.
- Menampilkan pengaduan berdasarkan ID.
- Memperbarui status pengaduan.
- Menghapus pengaduan.
- Validasi data input.
- Pembatasan kategori dan status menggunakan Enum.
- Dokumentasi API otomatis menggunakan Swagger UI.
- Unit testing menggunakan Pytest.

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman |
| FastAPI | Framework untuk membangun REST API |
| Uvicorn | ASGI server untuk menjalankan FastAPI |
| Pydantic | Validasi dan kontrak data |
| Pytest | Unit testing |
| Git | Version control |
| GitHub | Repository source code |

---

## Struktur Project

Project menggunakan pendekatan modular agar setiap bagian memiliki tanggung jawab yang berbeda.

```text
public-complaint-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── complaint_repository.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── complaints.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── complaint.py
│   │
│   └── services/
│       ├── __init__.py
│       └── complaint_service.py
│
├── tests/
│   └── test_complaints.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Penjelasan Struktur

#### `app/main.py`

Merupakan entry point aplikasi FastAPI.

File ini digunakan untuk:

- Membuat instance FastAPI.
- Mengatur informasi API.
- Mendaftarkan router.
- Menjalankan konfigurasi utama aplikasi.

#### `app/routers/`

Berisi endpoint atau route API.

File:

```text
complaints.py
```

bertanggung jawab menangani request HTTP yang berkaitan dengan pengaduan masyarakat.

#### `app/schemas/`

Berisi **contract data** API menggunakan Pydantic.

File:

```text
complaint.py
```

mendefinisikan:

- Struktur request.
- Struktur response.
- Kategori pengaduan.
- Status pengaduan.
- Validasi data.

#### `app/services/`

Berisi business logic aplikasi.

File:

```text
complaint_service.py
```

bertanggung jawab terhadap proses pengolahan data pengaduan sebelum diteruskan ke repository.

#### `app/repositories/`

Berisi bagian yang bertanggung jawab terhadap penyimpanan dan pengambilan data.

File:

```text
complaint_repository.py
```

digunakan untuk melakukan operasi terhadap data pengaduan.

#### `tests/`

Berisi unit test untuk menguji endpoint dan fungsi API.

File:

```text
test_complaints.py
```

digunakan untuk menguji apakah API memberikan response yang sesuai dengan kondisi yang diharapkan.

---

# Contract Data

Contract data diterapkan menggunakan **Pydantic BaseModel** pada:

```text
app/schemas/complaint.py
```

Contract request untuk membuat pengaduan menggunakan:

```python
class ComplaintCreate(BaseModel):
    citizen_name: str
    title: str
    description: str
    category: ComplaintCategory
    location: str
```

Sedangkan contract response menggunakan:

```python
class ComplaintResponse(BaseModel):
    id: int
    citizen_name: str
    title: str
    description: str
    category: ComplaintCategory
    location: str
    status: ComplaintStatus
```

Dengan contract tersebut, API dapat memastikan data yang diterima dan dikembalikan memiliki struktur yang sesuai.

---

# Kategori Pengaduan

API menyediakan beberapa kategori pengaduan:

```text
infrastruktur
pelayanan_publik
kebersihan
kesejahteraan
```

Contoh:

```json
{
  "category": "infrastruktur"
}
```

---

# Status Pengaduan

Status pengaduan yang tersedia:

```text
diajukan
diproses
selesai
ditolak
```

Status awal pengaduan secara otomatis ditetapkan menjadi:

```text
diajukan
```

ketika pengaduan baru dibuat.

---

# Endpoint API

Base URL:

```text
http://127.0.0.1:8000
```

## 1. Membuat Pengaduan

### Endpoint

```http
POST /api/v1/complaints
```

### Request Body

```json
{
  "citizen_name": "Andi Saputra",
  "title": "Jalan Rusak di Lingkungan",
  "description": "Terdapat banyak lubang pada jalan yang mengganggu pengguna kendaraan.",
  "category": "infrastruktur",
  "location": "Jl. Persatuan"
}
```

### Response

```json
{
  "id": 1,
  "citizen_name": "Andi Saputra",
  "title": "Jalan Rusak di Lingkungan",
  "description": "Terdapat banyak lubang pada jalan yang mengganggu pengguna kendaraan.",
  "category": "infrastruktur",
  "location": "Jl. Persatuan",
  "status": "diajukan"
}
```

---

## 2. Menampilkan Semua Pengaduan

### Endpoint

```http
GET /api/v1/complaints
```

Endpoint ini digunakan untuk mendapatkan seluruh data pengaduan yang tersimpan.

---

## 3. Menampilkan Pengaduan Berdasarkan ID

### Endpoint

```http
GET /api/v1/complaints/{complaint_id}
```

Contoh:

```http
GET /api/v1/complaints/1
```

Endpoint ini digunakan untuk mendapatkan satu data pengaduan berdasarkan ID.

---

## 4. Memperbarui Status Pengaduan

### Endpoint

```http
PATCH /api/v1/complaints/{complaint_id}/status
```

Contoh:

```http
PATCH /api/v1/complaints/1/status
```

### Request Body

```json
{
  "status": "diproses"
}
```

Status dapat diubah menjadi salah satu nilai yang tersedia:

```text
diajukan
diproses
selesai
ditolak
```

---

## 5. Menghapus Pengaduan

### Endpoint

```http
DELETE /api/v1/complaints/{complaint_id}
```

Contoh:

```http
DELETE /api/v1/complaints/1
```

Endpoint ini digunakan untuk menghapus pengaduan berdasarkan ID.

---

# Dokumentasi Swagger

FastAPI menyediakan dokumentasi API secara otomatis menggunakan Swagger UI.

Setelah server dijalankan, buka:

```text
http://127.0.0.1:8000/docs
```

Melalui Swagger UI, pengguna dapat:

- Melihat seluruh endpoint.
- Melihat struktur request dan response.
- Melakukan pengujian endpoint.
- Melihat validasi contract data.
- Mengirim request secara langsung tanpa aplikasi tambahan.

---

# Instalasi

## 1. Clone Repository

Clone repository menggunakan Git:

```bash
git clone <URL-REPOSITORY-GITHUB>
```

Kemudian masuk ke folder project:

```bash
cd public-complaint-api
```

---

## 2. Membuat Virtual Environment

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment pada Windows:

```powershell
venv\Scripts\activate
```

Jika berhasil, terminal akan menampilkan:

```text
(venv)
```

---

## 3. Install Dependency

Install seluruh library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

---

# Menjalankan Aplikasi

Pastikan virtual environment sudah aktif.

Kemudian jalankan:

```bash
python -m uvicorn app.main:app --reload
```

Jika berhasil, akan muncul:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
INFO: Application startup complete.
```

API dapat diakses melalui:

```text
http://127.0.0.1:8000
```

Dokumentasi Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Unit Testing

Unit test dibuat menggunakan **Pytest**.

Test berada pada:

```text
tests/test_complaints.py
```

Untuk menjalankan seluruh unit test:

```bash
pytest
```

Contoh hasil pengujian yang diharapkan:

```text
============================= test session starts =============================

collected 4 items

tests/test_complaints.py ....                                    [100%]

============================== 4 passed ==============================
```

Tanda:

```text
....
```

menunjukkan bahwa empat test berhasil dijalankan.

Unit test mencakup beberapa skenario, antara lain:

1. Pengujian pembuatan pengaduan.
2. Pengujian pengambilan seluruh pengaduan.
3. Pengujian pengaduan dengan ID yang tidak ditemukan.
4. Pengujian validasi data pengaduan yang tidak valid.

---

# Konsep Modular

Project ini menggunakan pemisahan tanggung jawab berdasarkan modul.

Alur request secara umum:

```text
Client
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Data
```

Sedangkan contract data digunakan pada proses request dan response:

```text
Client
   │
   │ Request JSON
   ▼
Schema / Pydantic
   │
   │ Validasi
   ▼
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Response
   │
   ▼
Schema / Pydantic
   │
   ▼
Client
```

Pembagian tersebut membuat kode lebih mudah dipahami, diuji, dan dikembangkan.

---

# Version Control dengan Git

Project menggunakan Git untuk mengelola perubahan source code.

Inisialisasi Git:

```bash
git init
```

Tambahkan seluruh file:

```bash
git add .
```

Buat commit:

```bash
git commit -m "Initial public complaint API"
```

Hubungkan dengan repository GitHub:

```bash
git remote add origin <URL-REPOSITORY-GITHUB>
```

Kemudian push:

```bash
git branch -M main
git push -u origin main
```

---

# `.gitignore`

File dan folder yang tidak perlu di-upload ke GitHub sebaiknya dimasukkan ke `.gitignore`.

Contoh:

```text
venv/
__pycache__/
*.pyc
.pytest_cache/
.env
```

Dengan demikian, virtual environment dan file cache Python tidak ikut masuk ke repository.

---

# Contoh Alur Penggunaan API

Contoh alur penggunaan sistem:

```text
1. Masyarakat mengirim pengaduan
              │
              ▼
2. API menerima request
              │
              ▼
3. Pydantic melakukan validasi
              │
              ▼
4. Router meneruskan request
              │
              ▼
5. Service memproses business logic
              │
              ▼
6. Repository menyimpan data
              │
              ▼
7. API mengembalikan response
              │
              ▼
8. Status awal = "diajukan"
```

Petugas kemudian dapat memperbarui status pengaduan:

```text
diajukan
    │
    ▼
diproses
    │
    ▼
selesai
```

atau:

```text
diajukan
    │
    ▼
ditolak
```

---

# Kesimpulan

Public Complaint API merupakan backend REST API berbasis FastAPI yang digunakan untuk mengelola pengaduan masyarakat.

Project ini menerapkan:

- **Modular Architecture** melalui pemisahan `routers`, `services`, `repositories`, dan `schemas`.
- **Contract Data** melalui Pydantic untuk menentukan struktur serta validasi request dan response.
- **Unit Testing** menggunakan Pytest untuk menguji fungsi API.
- **Git** sebagai version control untuk mengelola source code dan mengunggah project ke GitHub.

Project ini dibuat untuk memenuhi tugas mata kuliah **Pemrograman Lanjut** sekaligus sebagai implementasi dasar pengembangan backend menggunakan Python dan FastAPI.