print("=" * 40)
print("    DAILY SUCCESS TRACKER")
print("=" * 40)

score = 0
total_habits = 6

name = input("What is your name? ")
print()

print("welcome", name + "!")
print("Let's see how your day went!")
gym = input("Did you go to the gym today? (yes/no) ")
if gym == "yes":
    score = score +  1
reading = input("Did you read a book today? (yes/no) ")
if reading == "yes":
    score = score + 1
content = input("Did you feel content today? (yes/no) ")
if content == "yes":
    score = score + 1
meditation = input("Did you meditate today? (yes/no) ")
if meditation == "yes":
    score = score + 1

ai_learning = input("Did you learn something about AI today? (yes/no) ")
if ai_learning == "yes":
    score = score + 1

coding = input("Did you do any coding today? (yes/no) ")
if coding == "yes":
    score = score + 1

print()

print("Today's Summary")
print(".....................")
print("Gym:", gym)
print("Reading:", reading)
print("Content:", content)
print("Meditation:", meditation)
print("AI Learning:", ai_learning)
print("Coding:", coding)
print()
print("Today's Score:", score, "/6")
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

