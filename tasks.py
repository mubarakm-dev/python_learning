
task_db = []

while True:
        
    print("""Task Management System
        1. Add task
        2. View Task
        3. Edit Task
        4. Delete task
    """)

    choice = input("Enter choice: ")
    if choice == "1":
        task_name = input("Enter task: ")
        task_start_date = input("Enter task date: ")
        task_deadline = input("Enter task deadline: ")
        task_desc = input("Enter task description: ")

        save_task ={
        "task_name": task_name,
        "task_start_date": task_start_date,
        "task_deadline": task_deadline,
        "task_description":task_desc
        }
        task_db.append(save_task)
        harmony = task_db[0] # we want to access the first dict in the list, to access it rhough a variable, we will use the key
        print(f"""
            task: {harmony["task_name"]}
            date = {harmony["task_start_date"]}
            deadline: {harmony["task_deadline"]}
            description:  {harmony["task_description"]}
        """)

    elif choice == "2":
        harmony = task_db[0]
        print(f"""
                    task: {harmony["task_name"]}
                    date = {harmony["task_start_date"]}
                    deadline: {harmony["task_deadline"]}
                    description:  {harmony["task_description"]}
                """)


    elif choice == "5":
        print("Good bye")
        break


# zeller's congruence 