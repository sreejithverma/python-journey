def show_menu():
    print("\n" + "=" * 35)
    print("    DAILY SUCCESS TRACKER")
    print("=" * 35)
    print("1. Daily check-ins")
    print("2. View previous records")
    print("3. Statistics (coming soon)")
    print("4. Exit")
    print("=" * 35)

from tracker import SuccessTracker
import storage
from history import show_history




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
while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.ask()
        tracker.calculate()
        tracker.show()
        tracker.save()

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Statistics - Coming Soon")

    elif choice == "4":
        print("Goodbye Boss!")
        break

    else:
        print("Invalid choice. Please try again.")



