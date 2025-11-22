from colorama import Fore, init, Style
init(autoreset=True)
def sort_tasks_by_deadline(tasks):
    tasks=sorted(tasks, key=lambda x:x["deadline"])
    return tasks
def print_weekly_report(user, tasks, productivity, rating, rating_tag, tip, tip_tag):
    color={
    "High":Fore.RED,
    "Medium":Fore.BLUE,
    "Low":Fore.MAGENTA
}

    print("\n       WEEKLY REPORT")
    print(f"Name: {user['name']}")
    print(f"Total tasks: {user['total_tasks']}")
    print(f"Completed tasks: {user['tasks_completed']}")
    print(f"Remaining tasks: {user['total_tasks'] - user['tasks_completed']}")

    print(f"\nProductivity: {productivity:.2f}%")
    print(f"Rating: {rating_tag} {rating}")
    print(f"Improvement tip: {tip_tag} {tip}")
    print("\nTASK LIST:")
    for t in tasks:
     status = "Completed" if t["completed"] else "Pending"
     tag=color.get(t["priority"],"")
     print(f" {tag}{t['name']}{Style.RESET_ALL} | Deadline: {t['deadline']} | {t['priority']} | {status}")

    print("\nTOTAL TIME SPENT:")
    print(f" Time spent on tasks: {user['time_tasks']} hours")
    print(f" Time spent on other activities: {user['time_other_activities']} hours")