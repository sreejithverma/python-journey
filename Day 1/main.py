print("=" * 40)
print("    DAILY SUCCESS TRACKER")
print("=" * 40)

name = input("What is your name? ")
print()

print("welcome", name + "!")
print("Let's see how your day went!")

score = 0
habits = ["Gym", "Reading", "Content", "Meditation", "AI Learning", "Coding", "Networking"]
total_habits = len(habits)
for habit in habits:
    answer = input(f"Did you do {habit} today? (yes/no) ")
    if answer == "yes":
        score = score + 1

print()

print("Today's Summary")
print(".....................")
print("Today's Score:", score, "/7")
percentage = (score / total_habits) * 100
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

