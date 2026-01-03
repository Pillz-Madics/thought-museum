import interact
from logic import ThoughtManager
import time
import sys
import os

class ThoughtApp:
    def __init__(self):
        self.manager = ThoughtManager()
        

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(interact.generate_home_menu())
        action = input("Select an option: ")
        if action == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.create_thought()
        elif action == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            thoughts = self.list_thoughts()
            print(interact.generate_thoughts_list_view(thoughts))
            thought_id = input("Enter thought ID to view: ")
            self.view_thought(thought_id)
        elif action == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exiting...")
            time.sleep(1)
            sys.exit(0)
        else:
            print("Invalid option selected.")
            self.run()


    def create_thought(self):
        title = input("Enter thought title: ")
        content = input("Enter thought content: ")
        self.manager.create_thought(title, content)
        print(interact.generate_create_thought_view())
        time.sleep(1)
        self.run()

    def view_thought(self, thought_id):
        thought = self.manager.view_thought(thought_id)
        if thought:
            print(interact.generate_thought_view(thought))
        print("Thought not found.")
        

    def edit_thought(self, thought_id, new_title=None, new_content=None):
        return self.manager.edit_thought(thought_id, new_title, new_content)

    def delete_thought(self, thought_id):
        return self.manager.delete_thought(thought_id)

    def list_thoughts(self):
        return self.manager.list_thoughts()
    
if __name__ == "__main__":
    app = ThoughtApp()
    app.run()