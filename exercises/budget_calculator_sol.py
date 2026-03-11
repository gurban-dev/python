def compute_savings(income=None, expenses=None):
    if not income:
        income = int(input("Please input monthly income: "))

    if not expenses:    
        expenses = int(input("Please input expenses: "))
   
    savings = income - expenses
       
    if savings < 1:
        print("You didn't save anything.")
    else:
        print(f"You saved {savings} this month" )

    return savings

savings = compute_savings()

print("\nsavings:", savings)

compute_savings(income=100, expenses=50)