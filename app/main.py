from fastapi import FastAPI

from app.routers.complaints import router as complaint_router


app = FastAPI(
    title="Public Complaint API",
    description="API untuk pengelolaan pengaduan masyarakat",
    version="1.0.0"
)


app.include_router(complaint_router)


@app.get("/")
def root():
    return {
        "message": "Public Complaint API is running"
    }