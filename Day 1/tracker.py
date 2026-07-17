import json
from datetime import date
import storage


class SuccessTracker:
   def __init__(self, name, habits):
       self.name = name
       self.habits = habits
       self.score = 0
       self.percentage = 0

   def ask(self):
       
        for name, habit in self.habits.items():
           while True:
            answer = input(f"Did you do {name} today? (yes/no) ")
            if answer == "yes":
               habit["completed"] = True
               self.score = self.score+ 1
               break    
            elif answer == "no":
                break
           
            else:
             print("Invalid input. Please enter 'yes' or 'no'.")
        return self.score
        
        
   
   def calculate(self):
        self.percentage = (self.score / len(self.habits)) * 100
        self.percentage = round(self.percentage, 2)
        return self.percentage
   
   def show(self):  
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


   def load(self):
    self.history = storage.load()

   
    
   def save(self): 
       todayresult = {
          "date": str(date.today()),
          "name": self.name,
          "score": self.score,
          "percentage": self.percentage
     }
       self.history.append(todayresult)

       storage.save(self.history)
   
       
         