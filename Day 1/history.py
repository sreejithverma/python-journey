from storage import load

def show_history():
    history = load()
    print(history)  
    print(type(history))
    if not history:
        print("No history found.")
        return 
    
    show_dates(history)

    selected_date = select_date(history)
    print("Selected:", selected_date)

    if selected_date is None:
        return

    display_day(history, selected_date)
  
def show_dates(history):
   for record in history:
        print(record["date"])

def select_date(history):
        while True:
          choice = input("Enter a date to view details (YYYY-MM-DD) or 'q' to quit: ")
          if choice.lower() == 'q':
                return None
        
          print("Returning choice")
          return choice

def display_day(history, selected_date):
    for record in history:
        if record["date"] == selected_date:
            print(f"Date: {record['date']}")
            print(f"Name: {record['name']}")
            print(f"Score: {record['score']}")
            print(f"Percentage: {record['percentage']}%")
            return
    print("No record found for that date.")