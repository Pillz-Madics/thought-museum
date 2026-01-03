# Generate home menu for the interaction system home menu for the interaction system
def generate_home_menu():   
    """
    Generate the home menu for the interaction system.
    """
    
    return "Welcome to the Thought Management System!\n" \
           "1. Create New Thought\n" \
           "2. View Thoughts\n" \
           "3. Exit\n"

# Generates a note view for a given thought
def generate_thought_view(thought):
    '''
    Docstring for generate_thought_view
    
    :param thought: Description
    '''
    return f"tought View:\nTitle: {thought['title']}\nThought: {thought['content']}" \
            "1. Edit Thought\n" \
            "2. Delete Thought\n" \
            "3. Back to Home\n"


 # Generate a view confirming thought creation
def generate_create_thought_view():
    '''
    Docstring for generate_create_thought_view
    '''
    return "Thought successfully created!"

# Generate a list view of all thoughts
def generate_thoughts_list_view(thoughts):
    '''
    Docstring for generate_thoughts_list_view
    
    :param thoughts: Description
    '''
    thought_items = "Thoughts List:\n"

    for thought in thoughts:
        thought_items += thought + "\n"

    return thought_items