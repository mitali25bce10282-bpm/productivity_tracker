from colorama import Fore
def calculate_productivity(user):
    productivity=(user["tasks_completed"]/user["total_tasks"])*100
    return productivity
def get_rating(productivity):
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
    return rating, rating_tag
def get_tip(user):
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
    return tip, tip_tag