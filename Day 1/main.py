from tracker import SuccessTracker
import storage


print(storage.__file__)
print(dir(storage))

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






habits  = collect_habits()

tracker = SuccessTracker(name, habits)

tracker.load()
tracker.ask()
tracker.calculate()
tracker.show()
tracker.save()

