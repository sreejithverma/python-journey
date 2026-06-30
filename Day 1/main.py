print("=" * 40)
print("    DAILY SUCCESS TRACKER")
print("=" * 40)

score = 0
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

print()

print("Today's Summary")
print(".....................")
print("Gym:", gym)
print("Reading:", reading)
print("Content:", content)
print("Meditation:", meditation)
print()
print("Today's Score:", score, "/4")
