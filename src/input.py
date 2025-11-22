def collect_user_and_tasks():
    user = {}
    user["name"] = input("Enter your name:")
    user["total_tasks"] = int(input("Enter the total number of tasks for the week:"))

    tasks = []

    for i in range(user["total_tasks"]):
        print(f"\nTask {i+1}:")
        task_name = input("Name of the task:")
        deadline = input("Enter the deadline as YYYY-MM-DD:")
        priority = input("Priority (High/Medium/Low):").capitalize()

        tasks.append({
            "name": task_name,
            "deadline": deadline,
            "priority": priority,
            "completed": False
        })

    user["tasks_completed"] = int(input("\nHow many tasks have you completed?:"))

    for i in range(min(user["tasks_completed"], user["total_tasks"])):
        tasks[i]["completed"] = True

    return user, tasks
