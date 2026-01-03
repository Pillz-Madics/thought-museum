# Create a note class for a single thought
class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }