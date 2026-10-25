from app.repositories.complaint_repository import ComplaintRepository
from app.schemas.complaint import ComplaintStatus


class ComplaintService:

    def __init__(self, repository: ComplaintRepository):
        self.repository = repository

    def create_complaint(self, complaint):
        data = complaint.model_dump()

        data["status"] = ComplaintStatus.DIAJUKAN

        return self.repository.create(data)

    def get_all_complaints(self):
        return self.repository.get_all()

    def get_complaint(self, complaint_id):
        return self.repository.get_by_id(complaint_id)

    def update_status(self, complaint_id, status):
        complaint = self.repository.get_by_id(complaint_id)

        if complaint is None:
            return None

        complaint["status"] = status

        return complaint

    def delete_complaint(self, complaint_id):
        return self.repository.delete(complaint_id)