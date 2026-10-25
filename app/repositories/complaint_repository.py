class ComplaintRepository:

    def __init__(self):
        self.complaints = []
        self.next_id = 1

    def create(self, complaint):
        complaint["id"] = self.next_id
        self.next_id += 1

        self.complaints.append(complaint)

        return complaint

    def get_all(self):
        return self.complaints

    def get_by_id(self, complaint_id):
        for complaint in self.complaints:
            if complaint["id"] == complaint_id:
                return complaint

        return None

    def delete(self, complaint_id):
        complaint = self.get_by_id(complaint_id)

        if complaint is None:
            return False

        self.complaints.remove(complaint)

        return True