import interact
from logic import ThoughtManager
import time
import sys
import os

class ThoughtApp:
    def __init__(self):
        self.manager = ThoughtManager()

    def load_thoughts(self):
        """
        Docstring for load_thoughts
        
        :param self: Load thoughts from a file if it exists
        """
        if os.path.exists('thought_museum.txt'):
            self.manager.load_thoughts('thought_museum.txt')
        else:
            print("No existing thought museum found. Starting fresh.")

    def run(self):
        """
        Docstring for run
        
        :param self: Run the main application loop
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(interact.generate_home_menu())
        action = input("Select an option: ")
        if action == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.create_thought()
            self.run()
        elif action == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            thoughts = self.list_thoughts()
            print(interact.generate_thoughts_list_view(thoughts))
            thought_id = input("Enter thought ID to view or B for back: ")
            if thought_id == 'B' or thought_id == 'b':
                self.run()
            else:  
                self.view_thought(int(thought_id))
        elif action == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            if thoughts := self.list_thoughts():
                self.manager.save_thoughts('thought_museum.txt')
                print("Thoughts saved to thought_museum.txt")
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

    def view_thought(self, thought_id):
        thought = self.manager.view_thought(thought_id)
        if thought:
            print(interact.generate_thought_view(thought))
            options = input("Select an option: ")
            if options == '1':
                self.edit_thought(thought_id)
                print("Thought updated.")
                self.run()
            elif options == '2':
                self.delete_thought(thought_id)
                print("Thought deleted.")
                self.run()
            elif options == '3':
                self.run()
            else:
                print("Invalid option selected.")
                self.run()
        print("Thought not found.")
        time.sleep(1)
        self.run()
            
      
        

    def edit_thought(self, thought_id):
        self.manager.edit_thought(thought_id)

    def delete_thought(self, thought_id):
        self.manager.delete_thought(thought_id)

    def list_thoughts(self):
        return self.manager.list_thoughts()
    
if __name__ == "__main__":
    app = ThoughtApp()
    app.load_thoughts()
    app.run()