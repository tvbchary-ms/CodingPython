import os
# Add expenses
def add_expense(filename, amount, description):
    try:
        with open(filename,'a') as file:
            file.write(f"{amount}, {description}\n")
            print(f"Added expense: Rs.{amount} for {description}")

    except Exception as e:
        print("An Error occured! {e}")

# View Expenses
def view_expenses(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines() 
            total=0
            for line in lines:
                amount , description = line.strip().split(',')
                print(f"{description} - Rs.{amount}")
                total += float(amount)
            print(f"Total Expenses: Rs.{total}")
    except Exception as e:
        print(f"an error occurred: {e}")

def main():
    while(True):
        print("\n Simple Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input ("Enter your choice: ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                amount = float(input("Enter expense amount: Rs. "))
                description = input("Enter expense description: ")
                add_expense('expenses.txt', amount,description)
            except ValueError:
                print("please enter a valid number for amount")
        
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                view_expenses('expenses.txt')
            except Exception as e:
                print (f"Error occurred : {e}")
        
        elif choice =="3":
            print ("Goodbye!")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Choice is beyond range exiting program...! please try again")
            

if __name__== "__main__":
    main()