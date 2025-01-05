# TaskFlow

TaskFlow is a Python-based task management system designed to streamline how users handle, prioritize, and complete tasks. With interactive features, robust validation, and modular code, TaskFlow makes task management efficient and user-friendly.

## Features

- **Task Prioritization:** Assign priority levels using Fibonacci sequence logic (e.g., High, Medium, Low).
- **Interactive Menu:** Add, update, delete, and complete tasks through a user-friendly terminal interface.
- **Validation:** Ensures dates, priority levels, and other inputs are accurate and valid.
- **Comprehensive Functionality:** Includes features for listing tasks, marking them as completed, and providing detailed task information.
- **Scalability:** Modular design enables easy addition of new features.

## Tech Stack

- **Programming Language:** Python
- **Modules Used:** Standard Python libraries (no external dependencies)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TaskFlow.git

2. Navigate to the project directory:
   ```bash
   cd TaskFlow

3. Run the program:
   ```bash
   python main.py

## Usage
TaskFlow offers the following menu options:

- **A:** List all tasks (completed and pending)
- **L:** List only unfinished tasks
- **N:** Add a new task
- **U:**  Update an existing task
- **D:**  Delete a task
- **C:**  Mark a task as completed
- **Q:**  Quit the program

Example workflow:

1. Start the program by running python main.py.
2. Follow the menu prompts to manage your tasks.
3. View updates and changes dynamically in the terminal.

## Project Structure:
TaskFlow/
- main.py           # Entry point of the program
- functions.py      # Core task management logic
- extra_credit.py   # Additional utility functions (e.g., rank conversion)
- tests.py          # Unit tests for key functionalities

## Key Functions:
- **add_helper():** Allows users to add new tasks with details such as name, priority, and due date.
- **delete_task():** Removes a task from the list by ID.
- **update_task():** Updates fields (e.g., priority, due date) of an existing task.
- **rank_to_english():** Converts numerical task priority into human-readable text.
- **is_valid_date():** Validates date input in the MM/DD/YYYY format.

## Examples:
- **Adding a new task:**
::: Enter the task information:
* Enter at least 2 letters for the task name: Build a time machine
* Enter additional information for this task: Clean the parabolic reflectors
* Enter the priority of this task (1, 2, 3, 5, 8): 5
* Enter a valid date in the US date format (MM/DD/YYYY): 12/25/2040
* Is this task completed? y/n: n

-**Marking a task as completed:**
::: Mark a task as completed:
0 - Collect unicorn glitter - Task is Completed
1 - Build a time machine - Task is not Completed
Enter the number corresponding to the task ID to mark as completed: 1
Task marked as completed.

## Testing:
The tests.py file contains a comprehensive suite of unit tests. Run the tests with:
```bash
python -m unittest tests.py
