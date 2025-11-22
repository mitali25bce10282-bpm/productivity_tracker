from colorama import Fore, init, Style
init(autoreset=True)
#Dictionary to store user's information:
user = {}
user["name"] = input("Enter your name:")
user["total_tasks"] = int(input("Enter the total number of tasks for the week:"))
#List to store information about the tasks:
tasks = []
#Details for each task:
for i in range(user["total_tasks"]):
    print(f"\nTask {i+1}:")
    task_name = input("Name of the task:")
    deadline = input("Enter the deadline as YYYY-MM-DD:")
    priority=input("Priority (High/Medium/Low):").capitalize()

    tasks.append({"name": task_name, "deadline": deadline, "priority":priority, "completed": False})

user["tasks_completed"] = int(input("\nHow many tasks have you completed?:"))

for i in range(min(user["tasks_completed"], user["total_tasks"])):
    tasks[i]["completed"] = True
#Input for time
user["time_other_activities"] = float(input("\nHow many hours were spent on other activities?:"))
user["time_tasks"] = float(input("How many hours were spent on tasks?:"))
#Calculation of productivity
productivity = (user["tasks_completed"] / user["total_tasks"]) * 100
#Ratings:
rating_color={
    "Excellent. You are doing an amazing job. Keep going!":Fore.LIGHTMAGENTA_EX,
    "Nicely done. Great work! Stay consistent.":Fore.LIGHTYELLOW_EX,
    "Good. Don't give up! You'll do better.":Fore.LIGHTGREEN_EX,
    "Improvement required. It's high time! Let's improve!":Fore.LIGHTRED_EX
}
if productivity >= 80:
    rating = "Excellent. You are doing an amazing job. Keep going!"
    rating_tag=rating_color[rating]
elif productivity >= 60:
    rating = "Nicely done. Great work! Stay consistent."
    rating_tag=rating_color[rating]
elif productivity >= 50:
    rating = "Good. Don't give up! You'll do better."
    rating_tag=rating_color[rating]
else:
    rating = "Improvement Required. It's high time! Let's improve!"
    rating_tag=rating_color[rating]
#Tips
tip_color={
    "Improve":Fore.CYAN,
    "Balanced":Fore.GREEN
}
if user["time_other_activities"]>user["time_tasks"]:
    tip="Reduce distractions. You can do better!"
    tip_tag=tip_color["Improve"]
else:
    tip="Great balance!"
    tip_tag=tip_color["Balanced"]
#Sorting according to the deadlines
tasks=sorted(tasks, key=lambda x:x["deadline"])
#color tags based on priority
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