# main.py VICTOR ZHENG
from functions import *
from extra_credit import *

new_dict = {
    'A': 'List all tasks',
    'L': 'List unfinished tasks',
    'D': 'Delete a task',
    'N': 'Add a new task',
    'U': 'Update a task',
    'C': 'Mark a task as complete',
    'Q': 'Quit this program'} 
opt = None

test_tasks = [
    {
        "name": "Collect unicorn glitter",
        "info": "",
        "rank": 3,
        "due": '05/28/2042',
        "done": True
    },
    {
        'name': 'Build a time machine',
        'info': 'Clean the parabolic collector reflectors',
        'rank': 5,
        'due': '06/05/2042',
        'done': False
    },
    {
        "name": "Take a quantum leap",
        "info": "Ignore all safety rules for best results",
        "rank": 5,
        "due": '06/05/2042',
        "done": False
    }
]

while True:
    print("What would you like to do?")
    print_options(new_dict)
    opt = input("Enter a menu option\n::: ")
    opt = opt.upper() # to allow users to input lower- or upper-case letters

    if opt not in new_dict: 
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected {opt} to {new_dict[opt]}.") 

    if opt == 'Q': 
        print("Goodbye!\n")
        break 
    elif opt == "A":
        print_tasks_list(test_tasks, show_completed = True)
    elif opt == "L":
        print_tasks_list(test_tasks)
    elif opt == 'D':
        delete_helper(test_tasks)
    elif opt == 'N':
        add_helper(test_tasks)
    elif opt == 'U':
        update_helper(test_tasks)
    elif opt == 'C':
        complete_task(test_tasks)

    # ----------------------------------------------------------------
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a productive day!")
