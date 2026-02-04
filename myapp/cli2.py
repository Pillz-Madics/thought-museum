import argparse
from myapp.Thoughts.logic.logic import ThoughtManager
import os

class Thought_cli:
    def __init__(self):
        self.manager = ThoughtManager()
    
    def load(self):
        if os.path.exists("thoughts.txt"):
            self.manager.load_thoughts("thoughts.txt")
            
    def save(self):
        self.manager.save_thoughts("thoughts.txt")

    def create_thought(self, args):
        thought_title = input("Enter thought title: ")
        thought_body = input("Enter your thought: ")
        self.manager.create_thought(thought_title, thought_body)
        self.manager.save_thoughts("thoughts.txt")

    def list_thoughts(self, args):
        thoughts = self.manager.list_thoughts()
        print("Here lies your thoughts.\n")
        [print(f"{thought["id"]}. {thought["title"]}") for thought in thoughts]


    def view_thought(self, args):
        thought = self.manager.view_thought(args.open)
        if thought:
            print(f"Title:{thought["title"]}\n"\
                    f"{thought["content"]}")
        else: 
            print("Thought doesn't exist.")
        

    def edit_thought(self, args):
        self.manager.edit_thought(args.edit)

    
    def delete_thought(self, args):
        self.manager.delete_thought(args.delete)
        self.save()
    
    def create_parse(self):

        parser = argparse.ArgumentParser(description="Second implementation of cli")
        self.load()
        subparser = parser.add_subparsers(dest="command", required=True)

        create_parser = subparser.add_parser("create", description="Create thought")
        create_parser.add_argument("-c","--create", action="store_true")
        create_parser.set_defaults(func=self.create_thought)

        list_parser = subparser.add_parser("list", description="list thoughts")
        list_parser.add_argument("-l","--list", action="store_true")
        list_parser.set_defaults(func=self.list_thoughts)

        open_parser = subparser.add_parser("open", description="Open thought")
        open_parser.add_argument("-o","--open",  required=True, type=int)
        open_parser.set_defaults(func=self.view_thought)

        delete_parser = subparser.add_parser("delete", description="Delete thought")
        delete_parser.add_argument("-d","--delete", type=int)
        delete_parser.set_defaults(func=self.delete_thought)

        edit_parser = subparser.add_parser("edit", description="Edit thought")
        edit_parser.add_argument("-e","--edit", type=int)
        edit_parser.set_defaults(func=self.edit_thought)

        args = parser.parse_args()

        if hasattr(args, "func"):
            args.func(args)

def main():
        manager = Thought_cli()
        manager.create_parse()
if __name__ == "__main__":
    main()