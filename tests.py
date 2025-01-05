# tests.py VICTOR ZHENG
from functions import *
from extra_credit import *

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

# print_task(test_tasks[0], name_only = True)
# print_task(test_tasks[1])
# print_tasks_list(test_tasks, show_completed = True, name_only = True, show_idx = True)
# print_tasks_list(test_tasks, show_completed = True, name_only = True)
# print_tasks_list(test_tasks, show_completed = False, name_only = True)

# Assert statements for delete_helper function can't be done because input is user interactive

# Assert statements for delete_task
assert delete_task([], 1) == 0
assert delete_task([1, 2], 1) == -1
assert delete_task([1, 2], 5) == -1 # Test case for delete_task when the task ID is out of range

# Assert statements for is_valid_date
assert is_valid_date('02/29/2020') == True
assert is_valid_date('12/32/2010') == False
assert is_valid_date("'02/29/2020'") == False
assert is_valid_date('') == True #Empty String is valid
assert is_valid_date("13/45/2022") == False #Invalid Month
assert is_valid_date("invalid_date_format") == False #Invalid date format

# Assert statements for check_valid_field
assert check_valid_field('name', '') == 'name'
assert check_valid_field('name', 'Task') == 'valid' #Valid Name
assert check_valid_field('name', 'tada') == 'valid'
assert check_valid_field("info", "") == "valid" #Valid empty info
assert check_valid_field('rank', '') == 'valid'
assert check_valid_field('rank', '3') == 'valid'
assert check_valid_field('rank', '4') == 'rank'
assert check_valid_field('done', '') == 'done'
assert check_valid_field('done', 'y') == 'valid' #Valid done value
assert check_valid_field('due', '') == 'valid'
assert check_valid_field('due', '10/12/2023') == 'valid'
assert check_valid_field('due', '2/29/2023') == 'due' #Invalid leap year date
assert check_valid_field('money', '2000') == 'money'
assert check_valid_field('invalid_field', 'value') == "invalid_field" #Invalid field name

# Assert statements for get_new_task
assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'eiaou'}) == 'done'
assert get_new_task({'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done': 'n'}) == {'name': 'Read', 'info': 'Tolkien', 'rank': '2', 'due': '09/21/2013', 'done':False}
assert get_new_task({'name': 'Task', 'info': '', 'rank': '3', 'due': '12/31/2023', 'done': 'y'}) == {
    'name': 'Task', 'info': '', 'rank': '3', 'due': '12/31/2023', 'done': True}

# Assert statements for add_helper function can't be done because input is user interactive

# Assert statements for get_task function
assert get_task([], "0") == 0  # Empty List
assert get_task(["task1", "task2"], 1) == -1 # Invalid task_id_string
assert get_task([{'name': 'Task 1'}, {'name': 'Task 2'}], "-1") == -1  # Invalid task_id_string (not a valid integer)
assert get_task([{'name': 'Task 1'}, {'name': 'Task 2'}], "2") is None  # Invalid task_id_string (out of range)

#Assert statements for update_task function
assert update_task({'name': 'Task 1', 'info': 'Info 1', 'rank': 3, 'due': '12/31/2023', 'done': False}, 'name', 'Updated Task') == {'name': 'Updated Task', 'info': 'Info 1', 'rank': 3, 'due': '12/31/2023', 'done': False}  # Valid update
assert update_task({'name': 'Task 1', 'info': 'Info 1', 'rank': 3, 'due': '12/31/2023', 'done': False}, 'rank', 'invalid') == 'rank'  # Invalid update pertaining to "key"
assert update_task({'name': 'Read', 'info': 'Book', 'rank': 2, 'due': '12/31/2023', 'done': False}, 'info', 'New Book') == {'name': 'Read', 'info': 'New Book', 'rank': 2, 'due': '12/31/2023', 'done': False} #Valid update to "info" with a new value
assert update_task({'name': 'Write', 'info': 'Article', 'rank': 1, 'due': '12/15/2023', 'done': False}, 'done', 'y') == {'name': 'Write', 'info': 'Article', 'rank': 1, 'due': '12/15/2023', 'done': True} # Updating "done" to "y"

# Assert statements for update_helper function can't be done because input is user interactive

# Assert statements for rank_to_english function
assert rank_to_english(1) == "High"
assert rank_to_english(2) == "Medium"
assert rank_to_english(3) == "Low"
assert rank_to_english(5) == "Lowest"
assert rank_to_english(8) == "None"
assert rank_to_english(10) == "Unknown"

# Assert statements for complete_task can't be done because input is user interactive
