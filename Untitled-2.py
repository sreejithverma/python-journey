
while True:  
        try:
            age = int(input("Enter the age: "))
            if age>=18 and age<=100:
             print(f"You entered: {age}")
             break  # Exit the loop if input is valid
            
            else:
             print("Age must be between 18 and 100. Please try again.")
             
       
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        