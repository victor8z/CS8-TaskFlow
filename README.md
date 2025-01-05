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
```bash
TaskFlow/
├── main.py           # Entry point of the program
├── functions.py      # Core task management logic
├── extra_credit.py   # Additional utility functions (e.g., rank conversion)
├── tests.py          # Unit tests for key functionalities
