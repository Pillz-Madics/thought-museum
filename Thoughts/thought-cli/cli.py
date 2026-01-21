import argparse

commands = [
    {"command":"create",
     "help": "Create thought",
     "type": "str"},
     {"command":"list",
     "help": "List of thoughts",
     "type": "str"},
     {"command":"open",
     "help": "Open thought",
     "type": "int"},
     {"command":"edit",
     "help": "Edit thought",
     "type": "int"},
     {"command":"delete",
     "help": "delete thought",
     "type": "int"},
]

def parse_args(commands):
    parser = argparse.ArgumentParser(
        prog="Thought Museum",
        description="An archive of thinking."
    )

    for command in commands:
        parser.add_argument(command["command"], 
                            type=command["type"],
                            help=command["help"])
        
    
