#functions.py VICTOR ZHENG
from extra_credit import *

def print_options(options):
    """
    Given a dictionary, print the keys
    and values as the formatted options:
     {key} - {value}
    """
    for key, value in options.items():
        print(f" {key} - {value}")

######## LIST OPTION ########
def print_task(task, name_only = False):
    """
    param: task (dict) - a dictionary object that is
            assumed to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "rank": an integer, representing the task's priority
    - "due": a valid date-string in the US date format: 
            <MM>/<DD>/<YEAR>
    - "done": a Boolean representing whether a task is completed or not

    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields as requested.

    returns: None; only prints the task values
    """
    fields = ("info", "rank", "due", "done")
    print(f"{task['name']}") # the name of the task is always displayed
    if not name_only: # if we didn’t want to display only the name
        for field in fields:
                if field == "rank":
                    rank_english = rank_to_english(task["rank"])
                    print(f" * rank - {task[field]} = ({rank_english}) priority!")
                elif field == "due":
                    print(f" * due - {task[field]}")
                elif field == "done":
                    print(f" * done - {'True' if task[field] else 'False'}")
                else:
                    print(f" * {field.lower()} - {task[field]}")
            

def print_tasks_list(task_list, name_only = False,
                     show_completed = False, show_idx = False):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_completed (Boolean) - by default, set to False.
            If False, then only the unfinished tasks are shown.
            If True, all tasks (completed as well as unfinished) 
            are displayed.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx} - " before the
            task name.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*50)
    num_shown = 0
    for idx, task in enumerate(task_list): # process each task in the list
        if task["done"] == True and show_completed == False: 
            continue # skip completed tasks
        if show_idx: # if the index of the task needs to be displayed
            print(f"{idx} - ", end="") # Hint: idx need not be the same as num_shown and use enumerate at for loop above
        print_task(task, name_only)
        num_shown += 1
    print(f"Showing {num_shown} results")
    print("-"*50)

######## DELETE OPTION ########

def delete_helper(task_collection):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)

    The function warns the user and returns, if there's nothing to delete.
    The function displays all tasks to the user and interactively allows
    the user to select the task ID, which needs to be deleted.
    If an invalid option or a task ID was given, displays a warning and
    returns without modifying the collection.

    Helper functions:
    - print_tasks_list
    - print_task
    - delete_task

    returns: None; directly modifies task_collection to remove tasks.
    """
    if len(task_collection) == 0:
        print("WARNING: there is nothing to delete.")
        return

    print("Which task would you like to delete?")
    print_tasks_list(task_collection, name_only = True, show_idx = True, show_completed = True)
    print("::: Enter the number corresponding to the task ID")
    print("::: or enter A to delete all tasks in the collection.")
    user_input = input("> ")
    if user_input == "A": ### only accept upper-case
        task_collection.clear() # Delete all tasks
        print("Success! Deleted all tasks!")
        return
    elif user_input.isdigit() == False: ### if the user didn't enter a number
        print(f"WARNING: '{user_input}' is an invalid option!")
        return
    
    result = delete_task(task_collection, user_input)
    if type(result) == dict:
        print("Success! Deleted the task:")
        print_task(result)
    else: ### prints an error as the item with that ID is not found
        print(f"WARNING: '{user_input}' is not found!")


def delete_task(task_collection, task_id_string):
    """
    param: task_collection (list) - holds all tasks;
           an integer ID indexes each task (stored as a dictionary)
    param: task_id_string (str) - a string that is supposed to represent
           an integer ID that indexes the task in the list

    returns:
    0 - if the collection is empty.
    -1 - if the provided parameter is not a string or if it is not
    a valid integer >=0 representing the task’s position on the list.
    Otherwise, returns the item (dict) that was removed from the
    provided collection.
    """
    if len(task_collection) == 0:
        return 0
    
    if type(task_id_string) != str: #check if not a string
        return -1 

    if task_id_string.isdigit() == False: #check if integer
        return -1
    
    task_id = int(task_id_string)
    if task_id < 0 or task_id >= len(task_collection):
        return -1
    else:
        return task_collection.pop(task_id) #.pop returns the item from the dictionary that was removed from task_collection

### VALIDATION FUNCTIONS

def is_valid_year(date_list):
    """
    param: date_list (list) - A list containing the month, day, and year in order.

    The function checks if the year in the date_list is valid or exists.

    returns: True if the year is greater than or equal to 1000
    Otherwise returns False
    """
    year = int(date_list[2])
    return year >= 1000

def is_valid_month(date_list):
    """
    param: date_list (list) - A list containing the month, day, and year in order.

    The function checks if the month in the date_list is valid or exists.

    returns: True if the month is between 1 and 12 inclusively.
    Otherwise returns False.
    """
    month = int(date_list[0])
    return 1 <= month <= 12


def is_valid_day(date_list):
    """
    param: date_list (list) - A list containing the month, day, and year in order.

    The function checks if the day in the date_list is valid or exists with the given month and year.

    returns: True if the day in the date_list is valid or exists with the given month and year.
    Otherwise returns False.
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    month = int(date_list[0])
    day = int(date_list[1])

    if is_valid_month(date_list):
        if month == 2:
            # Check if the day is valid for February using the days_in_feb() function
            return 1 <= day <= days_in_feb(int(date_list[2]))
        else:
            # Check if the day is valid for other months
            days_in_month = {
                1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }
            return 1 <= day <= days_in_month[month]

    return False
  

def days_in_feb(user_year):
    """
    param: user_year (int) - The year the user inputted that will have the days calculated in February.

    The function calculates the number of days in February for the year the user inputted.

    returns: (int) - The number of days in February for the year the user inputted
    """
    
    if user_year % 400 == 0:
        return 29
    elif user_year % 100 == 0:
        return 28
    elif user_year % 4 == 0:
        return 29
    else:
        return 28

def is_valid_date(date_str):
    """
    param: date_str (str) - stores either an empty string
            or a date in the `MM/DD/YYYY` format

    If the string is not empty and has the 3 required
    date components, the function checks each date component
    using the helper functions.

    Helper functions:
    - is_valid_year - only checks the year (a str, only digits,
        contains 1000 or above)
    - is_valid_month - only checks the month (accepts both
        formats: when the month has a leading 0, e.g. "02"
        as well when it does not, e.g., just "2")
    - is_valid_day - checks that the month is valid before
        checking that day is also correct (calls days_in_feb()); 
        accepts both formats: when the day has a leading 0, 
        e.g. "07", as well when it does not, e.g., just "7"
    - days_in_feb - is called in is_valid_day() if the
        provided month is Feb to check if the given day
        is correct

    returns: True, if date_str is empty;
    returns False if the date_str does not have the 3 required
        date components (formed by splitting on the slash character);
    otherwise, returns a Boolean value based on the result
    of the helper functions.
    """
    if len(date_str) == 0:
        return True
    
    components = date_str.split('/')

    # Check if there are 3 components of the month
    if len(components) != 3:
        return False
    
    month_str, day_str, year_str = components

    # Check if the year, month, and day are integers
    if month_str.isdigit() == False or day_str.isdigit() == False or year_str.isdigit() == False:
        return False
    
    # Check if the year, month, and day are valid
    if not is_valid_year(components) or not is_valid_month(components) or not is_valid_day(components):
        return False
    
    return True
    

def check_valid_field(field, value):
    """
    param: field (str) - the name of a task field to validate
    param: value (str) - the proposed value for the field

    The function checks that the field is one of the
    expected keys. Expected fields stored in the function are
    ("name", "info", "rank", "due", "done").

    If the field is valid, the function checks that the provided
    value is the correct STRING value for the provided field:
    * `"name"`: a 2 or more characters string with the task’s name.
    * `"info"`: can be an empty string; no further validation is needed.
    * `"due"`: a string storing the date in the `MM/DD/YYYY` format.
        The string can be empty if the task has no due date.
        Checked using is_valid_date()
    * `"rank"`: a string which can be empty or contain one of five
        Fibonacci numbers ('1', '2', '3', '5', '8').
    * `"done"`: a string that contains “y” or “n”

    Helper functions:
    - is_valid_date

    returns:
    the name of the field if the field name is not found or
    if the value for a given field is invalid;
    otherwise, returns "valid"

    """
    expected_fields = ("name", "info", "rank", "due", "done")
    
    if field not in expected_fields: # Check if the field name detected as valid
        return field 

    # Check if the empty fields are correctly detected as valid
    if (field == "rank" or field == "due") and value == "":
        return "valid"

    # Validate the field based on the type of field it is
    if field == "name": # Checking if the length of the name is less than 2 characters long
        if len(value) >= 2:
            return "valid"

    elif field == "info": #Info field is always valid since it can be an empty string
        return "valid"

    elif field == "due": # Checking if date is valid 
        if is_valid_date(value):
            return "valid"

    elif field == "rank": # Checking if the rank is one of the Fibonacci numbers or an empty string
        if value in ('1', '2', '3', '5', '8'):
            return "valid"

    elif field == "done": # Checking if the done value is 'y' or 'n'
        if value in ("y", "n"):
            return "valid"

    return field

######## ADD OPTION ########

def add_helper(tasks_list):
    """
    param: tasks_list (list) - holds all tasks;
            each task is a dictionary.

    Collects the necessary information from the user and
    attempts to create a new task entry. If the provided
    information was valid, adds the new task to the list.
    Prints the added task via the print_task().
    Otherwise, prints a warning:
    "WARNING: trying to set '{result}' to an invalid option '{new_tasks[result]}'!"
    where the first ellipses map to a name of a field and
    the second one is the value that the user provided.

    Helper functions:
    - get_new_task
    - print_task
    - is_valid_date

    The function does not return anything.
    """
    new_tasks = {}  # Creating a temporary dictionary to hold user values

    task_fields = {
        "name": "* Enter at least 2 letters for the task name:",
        "info": f"* Enter additional information for this task:",
        "rank": f"* Enter the priority of this task (1, 2, 3, 5, 8):",
        "due": f"* Enter a valid date in the US date format (MM/DD/YEAR):",
        "done": f"* Is this task completed? y/n"
    }

    print("::: Enter the task information:")
    for key in task_fields:
        print(task_fields[key])  # display the prompt
        value = input("> ")  # get the data
        new_tasks[key] = value  # store it in the temporary dictionary

    result = get_new_task(new_tasks)  # Attempt to create a new task object
    if type(result) == dict:
        print("Success! Adding a new task:")
        tasks_list.append(result)  # Adding the dictionary that was returned
        print_task(result)  # Printing the task that was just added
    else:
        print(f"WARNING: trying to set '{result}' to an invalid option '{new_tasks[result]}'!")


def get_new_task(values_dict):
    """
    param: values_dict (dict) - a dictionary that holds
            STRING values for all keys

    Helper functions:
    - check_valid_field 

    For each key and value in the provided dictionary, calls
    the check_valid_field() to verify that they are valid.
    Does not modify values_dict.

    returns: a NEW dictionary that stores the values from the values_dict
        converted to the correct type / value, after each necessary value
        was verified by the check_valid_field().
        The only field that needs conversion is "done", since it is
        supposed to be stored as a Boolean.
    Otherwise, returns the name of the invalid key or the valid key that
    stores the invalid data.
    """
    for key, value in values_dict.items():
        if check_valid_field(key, value) != "valid":
            return key

    new_task_dict = values_dict.copy()  # Make a copy of the values

    # Converting the string to Boolean for the "done" field, with "y" giving a Boolean value of True and "n" giving a Boolean value of False
    if values_dict["done"].lower() == "y":
        new_task_dict["done"] = True
    elif values_dict["done"].lower() == "n":
        new_task_dict["done"] = False

    return new_task_dict

# UPDATE FUNCTION

def get_task(task_collection, task_id_string):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)
    param: task_id_string (str) - a string that is supposed to represent
            an integer ID that corresponds to a valid index in the
            collection

    returns:
    0 - if the collection is empty.
    -1 - if the provided parameter is not a string or if it is not
    a valid integer

    Otherwise, convert the provided string to an integer;
    returns None if the ID is not a valid index in the list
    or returns the existing item (dict) that was requested.
    """
    if len(task_collection) == 0: # Indicates an Empty List
        return 0
    
    if type(task_id_string) != str: # Check if not a string
        return -1
    
    if task_id_string.isdigit() == False: #Indicates it is not an integer
        return -1

    task_id = int(task_id_string)
    if task_id < 0 or task_id >= len(task_collection):
        return None
    else:
        return task_collection[task_id]

def update_task(task_dict, key, value):
    """
    param: task_dict (dict) - a valid task dictionary
    param: key (str) - a valid key in the dictionary
    param: value - a valid value, depending on the key

    Helper function:
    - check_valid_field - verifies the validity of the key
    and the value

    Note: Convert the value to Boolean if the key is 'done', based on if 'y' or 'n' is the value.
    Note: Remember that the field 'rank' is supposed to be stored as an integer.

    returns: the key if either the key or value is invalid;
    otherwise, returns an updated dictionary.
    """
    if check_valid_field(key, value) != "valid":
        return key

    # Convert the "done" value to Boolean
    if key == "done":
        value = value.lower() == "y"

    # Convert the "rank" value to an integer
    if key == "rank":
        value = int(value)

    task_dict[key] = value
    return task_dict

def update_helper(task_collection):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)

    Helper functions:
    - print_tasks_list
    - print_task
    - print_options
    - get_task
    - update_task

    The function does not return anything.    
    """
    if len(task_collection) == 0 :
        print("WARNING: there is nothing to update.")
        return

    print("Which task would you like to update?")
    print_tasks_list(task_collection, name_only = True, show_idx = True, show_completed = True)
    print("::: Enter the number corresponding to the task ID:")
    task_id_string = input("> ") # Get the user input

    task_to_update = get_task(task_collection, task_id_string)
    if type(task_to_update) == dict:
        print("Success! Found:")

        print_task(task_to_update, name_only = True) # Displaying only the name of the task
    elif task_to_update == 0:
        print("WARNING: there is nothing to update.")
        return
    elif task_to_update == -1:
        print(f"WARNING: '{task_id_string}' is an invalid option!")
        return
    else:
        print(f"WARNING: '{task_id_string}' is not found!")
        return

    print("Which field would you like to update?")
    print_options(task_to_update) # Display the selected task object: its keys and values
    print("::: Enter the field name:")
    field_name = input("> ") # Get the key as an input
    if field_name not in task_to_update:
        print(f"WARNING: '{field_name}' is an invalid field!")
        return

    print(f"::: Enter the {field_name} information instead of '{task_to_update[field_name]}':")
    new_value = input("> ") # Get the data

    updated_task = update_task(task_to_update, field_name, new_value) # Send the specific task to update
    if type(updated_task) == dict:
        print("Success!") 
        print_task(updated_task)
        # print(task_collection) ### DEBUGGING
    else:
        print(f"WARNING: trying to set '{field_name}' to an invalid value '{new_value}'!") # Error when trying to set the given key to an invalid value provided by the user

