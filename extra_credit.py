#extra_credit.py VICTOR ZHENG

def rank_to_english(rank):
    """
    param: rank (int) - numerical rank of the task

    The function will attach the numerical rank to its equivalent in English.
    Rank 1 would be high, and the higher the number is the lower the priority.

    returns: English equivalent of the rank ("high" or "low")
    """
    rank_attaching = {
        1: "High",
        2: "Medium",
        3: "Low",
        5: "Lowest",
        8: "None"
        # Attaching the rank (one of the Fibonacci numbers) to its English equivalent
    }

    # Return the attached value or Unknown message if rank not found
    if rank in rank_attaching:
        return rank_attaching[rank]
    else:
        return "Unknown"

def complete_task(task_collection):
    """
    param: task_collection (list) - holds all tasks;
            maps an integer ID/index to each task object (a dictionary)

    The function allows the user to mark a task as completed by inputting their desired task ID.

    returns: None; only prints the task values
    """
    if len(task_collection) == 0:  # Checks for an empty list
        print("WARNING: Empty Tasks List")
        return

    print("Mark a task as completed:")

    for idx, task in enumerate(task_collection):
        if task['done'] == True:
            completion_status = "Task is Completed"
        else:
            completion_status = "Task is not Completed"
        print(f"{idx} - {task['name']} - {completion_status}") # Show the task ID, name, and if it is completed before we mark it as complete

    task_id_string = input("Enter the number corresponding to the task ID to mark as completed: ")

    if task_id_string.isdigit():
        task_id = int(task_id_string)

        if 0 <= task_id < len(task_collection):
            task_to_complete = task_collection[task_id]

            if task_to_complete['done'] is False:
                task_to_complete['done'] = True
                print("Task marked as completed.")
            else:
                print("WARNING: Task is already marked as completed.")
        else:
            print("WARNING: Invalid option or task not found.")
    else:
        print(f"WARNING: '{task_id_string}' is an invalid option or not a number.")

    print("\nUpdated Task List:")
    for task in task_collection:
        print(f"\nTask: {task['name']}")
        print(f"Rank: {task['rank']} ({rank_to_english(task['rank'])})")
        print(f"Due: {task['due']}")
        print(f"Done: {'True' if task['done'] else 'False'}")
