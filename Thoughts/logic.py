from note import Note
# create a class for managing thoughts and their logic
class ThoughtManager:
    def __init__(self):
        self.thoughts = {}
        self.next_id = 1

    def create_thought(self, title, content):
        thought = Note(self.next_id, title, content)
        self.thoughts[self.next_id] = thought
        self.next_id += 1
        return thought.to_dict()

    def view_thought(self, thought_id):
        thought = self.thoughts.get(thought_id)
        if thought:
            return thought.to_dict()
        return None

    def edit_thought(self, thought_id, new_title=None, new_content=None):
        thought = self.thoughts.get(thought_id)
        if thought:
            if new_title:
                thought.title = new_title
            if new_content:
                thought.content = new_content
            return thought.to_dict()
        return None

    def delete_thought(self, thought_id):
        if thought_id in self.thoughts:
            del self.thoughts[thought_id]
            return True
        return False

    def list_thoughts(self):
        return [thought.to_dict() for thought in self.thoughts.values()]