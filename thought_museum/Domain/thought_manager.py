from .note import Note
import datetime



# create a class for managing thoughts and their logic
class ThoughtManager:
    def __init__(self):
        self.thoughts = {}
        self.next_id = 1

    def create_thought(self, title, content):
        """
        Docstring for create_thought

        :param self: function instance
        :param title: Name of the thought
        :param content: Content of the thought
        """
        thought = Note(self.next_id, title, content)
        self.thoughts[self.next_id] = thought
        self.next_id += 1
        return thought.to_dict()

    def view_thought(self, thought_id):
        """
        Docstring for view_thought

        :param self: function instance
        :param thought_id: ID of the thought to view
        """
        thought = self.thoughts.get(thought_id)
        if thought:
            return thought.to_dict()
        return None

    

    def edit_thought(self, thought):
        """ 
        Docstring for edit_thought
        :param self: function instance
        :param thought_id: ID of the thought to edit
        """
        old_thought = self.thoughts.get(thought.id)
        self.thoughts[thought.id] = thought

        if old_thought == self.thoughts.get(thought.id):
            return False
        else:
            return True
        
        

    def delete_thought(self, thought_id):
        """
        Docstring for delete_thought

        :param self: function instance
        :param thought_id: ID of the thought to delete
        """
        if thought_id in self.thoughts:
            del self.thoughts[thought_id]
            return True
        return False

    def list_thoughts(self):
        """
        Docstring for list_thoughts
        :param self: function instance
        """
        return [thought.to_dict() for thought in self.thoughts.values()]

