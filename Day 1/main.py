print("=" * 40)
print("    DAILY SUCCESS TRACKER")
print("=" * 40)

name = input("What is your name? ")
print()

print("welcome", name + "!")
print("Let's see how your day went!") 

class SuccessTracker:
   def __init__(self, habits):
       self.habits = habits
       self.score = 0
       self.percentage = 0

   def ask_questions(self):
       for habit_name, habit_data in self.habits.items():
           answer = input(f"Did you do {habit_name} today? (yes/no) ")
           if answer.lower() == "yes":
               habit_data["completed"] = True
               self.score = self.score+ 1
       return self.score
        
        
   
   def calculate_score(self):
        self.percentage = (self.score / len(self.habits)) * 100
        self.percentage = round(self.percentage, 2)
        return self.percentage
   
   def show_results(self):
        print()
        print("Today's Summary")
        print(".....................")
        print("Today's Score:", self.score)
        print("Today's Percentage:", self.percentage, "%")
        if self.percentage == 100:
         print("PEAK PRODUCTIVITY!")
         print(" One step closer to dream life!")
        elif self.percentage >= 80:
         print("Excellent work! Keep the momentum going!")   
        elif self.percentage >= 60:
         print("Good Productivity! Consistency beats perfection!")
        elif self.percentage >= 50:
         print("Average Productivity! Let's aim for more tomorrow!")
        elif self.percentage >= 30:
         print("Needs improvement! Reset tomorrow!")
        else:
         print("Today did not go as planned, The best time to reset is tomorrow!")

   def save_results(self):
    file = open("completed_habits.txt", "w")
    file.write("Today's score: " + str(self.score) + "\n")
    file.write("Today's percentage: " + str(self.percentage) + "%\n")
    file.write("\nCompleted Habits:\n")

    for habit_name, habit_data in self.habits.items():
     if habit_data["completed"]:
        file.write(habit_name + "\n")

    file.close()
   
def collect_habits():
       habits = {"Gym": {"completed": False, "weekly_targets": 5, "streak": 0},
                 "Meditation": {"completed": False, "weekly_targets": 7, "streak": 0},
                 "Reading": {"completed": False, "weekly_targets": 7, "streak": 0},
                 "Content Creation": {"completed": False, "weekly_targets": 5, "streak": 0},
                 "Networking": {"completed": False, "weekly_targets": 3, "streak": 0},
                 "Coding": {"completed": False, "weekly_targets": 5, "streak": 0}
                 }
       return habits 




habits  = collect_habits()

successtracker = SuccessTracker(habits)
successtracker.ask_questions()
successtracker.calculate_score()
successtracker.show_results()
successtracker.save_results()