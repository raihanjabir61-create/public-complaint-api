from pydantic import BaseModel, Field
from enum import Enum


class ComplaintCategory(str, Enum):
    INFRASTRUKTUR = "infrastruktur"
    PELAYANAN_PUBLIK = "pelayanan_publik"
    KEBERSIHAN = "kebersihan"
    KESEJAHTERAAN = "kesejahteraan"


class ComplaintStatus(str, Enum):
    DIAJUKAN = "diajukan"
    DIPROSES = "diproses"
    SELESAI = "selesai"
    DITOLAK = "ditolak"


class ComplaintCreate(BaseModel):
    citizen_name: str = Field(min_length=3, max_length=100)
    title: str = Field(min_length=5, max_length=150)
    description: str = Field(min_length=10)
    category: ComplaintCategory
    location: str = Field(min_length=3, max_length=200)


class ComplaintResponse(BaseModel):
    id: int
    citizen_name: str
    title: str
    description: str
    category: ComplaintCategory
    location: str
    status: ComplaintStatus


class ComplaintStatusUpdate(BaseModel):
    status: ComplaintStatus