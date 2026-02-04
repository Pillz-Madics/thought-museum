import datetime
# Create a note class for a single thought
class Note:
    def __init__(self, id, title, content, created_at = None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now() if created_at == None else created_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }