task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"'{task}' is a {priority} priority task"
match priority:
    case "high" | "medium" | "low":
        pass 
    case _:
        reminder = f"'{task}' has an unknown priority level"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."
print(f"Reminder: {reminder}")
