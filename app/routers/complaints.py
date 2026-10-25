from fastapi import APIRouter, HTTPException

from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintResponse,
    ComplaintStatusUpdate
)

from app.services.complaint_service import ComplaintService
from app.repositories.complaint_repository import ComplaintRepository


router = APIRouter(
    prefix="/api/v1/complaints",
    tags=["Complaints"]
)


repository = ComplaintRepository()
service = ComplaintService(repository)


@router.post(
    "",
    response_model=ComplaintResponse,
    status_code=201
)
def create_complaint(data: ComplaintCreate):

    return service.create_complaint(data)


@router.get(
    "",
    response_model=list[ComplaintResponse]
)
def get_complaints():

    return service.get_all_complaints()


@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def get_complaint(complaint_id: int):

    complaint = service.get_complaint(complaint_id)

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Pengaduan tidak ditemukan"
        )

    return complaint


@router.patch(
    "/{complaint_id}/status",
    response_model=ComplaintResponse
)
def update_status(
    complaint_id: int,
    data: ComplaintStatusUpdate
):

    complaint = service.update_status(
        complaint_id,
        data.status
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Pengaduan tidak ditemukan"
        )

    return complaint


@router.delete(
    "/{complaint_id}"
)
def delete_complaint(complaint_id: int):

    deleted = service.delete_complaint(complaint_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Pengaduan tidak ditemukan"
        )

    return {
        "message": "Pengaduan berhasil dihapus"
    }