from note import Note
import datetime
import readline
# create a class for managing thoughts and their logic
class ThoughtManager:
    def __init__(self):
        self.thoughts = {}
        self.next_id = 1

    def create_thought(self, title, content):
        """
        Docstring for create_thought
        
        :param self: fuction instance
        :param title: Name of the thought
        :param content: Content of the thought
        """
        thought = Note(self.next_id, title, content)
        self.thoughts[self.next_id] = thought
        self.next_id += 1
        print(self.thoughts)
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
    
    def pre_hook(self, text):
        """
        Docstring for pre_hook
        
        :param self: function instance
        :param text: Text to prefill
        """
        def prefill():
            readline.insert_text(text)
            readline.redisplay()
        readline.set_pre_input_hook(prefill)
    
    def edit_thought(self, thought_id):
        """"
        Docstring for edit_thought
        :param self: function instance
        :param thought_id: ID of the thought to edit
        """

        thought = self.thoughts.get(thought_id)
        if thought:
            self.pre_hook(thought.title)
            title = input("Enter new title: ")

            thought.title = title
            self.pre_hook(thought.content)
            content = input("Enter new content: ")
            thought.content = content

            readline.set_pre_input_hook(None)
        else:
            return "Thought not found."
        return None

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
    
    def save_thoughts(self, filename):
        """
        Docstring for save_thoughts
        
        :param self: function instance
        :param filename: Name of the file to save thoughts
        """
        with open(filename, 'w') as f:
            for thought in self.thoughts.values():
                f.write(f"{thought.id}|{thought.title}|{thought.content}|{thought.created_at}\n")
    
    def load_thoughts(self, filename):
        """
        Docstring for load_thoughts
        
        :param self: function instance
        :param filename: Name of the file to load thoughts from
        """
        try:
            with open(filename, 'r') as f:
                for line in f:
                    id_str, title, content, created_at_str = line.strip().split('|')
                    print(f" first print: {id_str}", f"second:{title}", f"third: {content}", f"fourth: {created_at_str}")
                    thought_id = int(id_str)
                    created_at = datetime.datetime.fromisoformat(created_at_str)
                    thought = Note(thought_id, title, content, created_at)
                    self.thoughts[thought_id] = thought
                    if thought_id >= self.next_id:
                        self.next_id = thought_id + 1
        except FileNotFoundError:
            pass