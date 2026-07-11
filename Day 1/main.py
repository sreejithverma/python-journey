print("=" * 40)
print("    DAILY SUCCESS TRACKER")
print("=" * 40)

name = input("What is your name? ")
print()

print("welcome", name + "!")
print("Let's see how your day went!")

def collect_habits():
       habits = {"Gym": {"completed": False, "weekly_targets": 5, "streak": 0},
                 "Meditation": {"completed": False, "weekly_targets": 7, "streak": 0},
                 "Reading": {"completed": False, "weekly_targets": 7, "streak": 0},
                 "Content Creation": {"completed": False, "weekly_targets": 5, "streak": 0},
                 "Networking": {"completed": False, "weekly_targets": 3, "streak": 0},
                 "Coding": {"completed": False, "weekly_targets": 5, "streak": 0}
                 }
       return habits 

def ask_questions(habits):
    score = 0
    for habit_name, habit_data in habits.items():
        answer = input(f"Did you do {habit_name} today? (yes/no) ")
        if answer == "yes":
            habit_data["completed"] = True
            score = score + 1
    return score

def calculate_score(score, habits):
    percentage = (score / len(habits)) * 100
    percentage = round(percentage, 2)
    return percentage

def show_results(score, percentage, habits):
    print()
    print("Today's Summary")
    print(".....................")
    print("Today's Score:", score)
    print("Today's Percentage:", percentage, "%")
    if percentage == 100:
     print("PEAK PRODUCTIVITY!")
     print(" One step closer to dream life!")
    elif percentage >= 80:
     print("Excellent work! Keep the momentum going!")   
    elif percentage >= 60:
     print("Good Productivity! Consistency beats perfection!")
    elif percentage >= 50:
     print("Average Productivity! Let's aim for more tomorrow!")
    elif percentage >= 30:
     print("Needs improvement! Reset tomorrow!")
    else:
     print("Today did not go as planned, The best time to reset is tomorrow!")

    file = open("completed_habits.txt", "w")
    file.write("Today's score: " + str(score) + "\n")
    file.write("Today's percentage: " + str(percentage) + "%\n")
    file.write("\nCompleted Habits:\n")

    for habit_name, habit_data in habits.items():
     if habit_data["completed"]:
        file.write(habit_name + "\n")
    
    
    file.close()


habits = collect_habits()

score = ask_questions(habits)

percentage = calculate_score(score, habits)

show_results(score, percentage, habits)
