# Student Weekly Expense Calculator (Extended - Week 3)
# Calculates transport, feeding, and total weekly expenses,
# then compares against a weekly budget.

def main():
    # Get student name (string)
    student_name = input("Enter student name: ").strip()

    # Get daily transport cost (whole naira - int)
    daily_transport = int(input("Enter daily transport cost (NGN): "))

    # Get daily feeding cost (whole naira - int)
    daily_feeding = int(input("Enter daily feeding cost (NGN): "))

    # Get number of days on campus (integer)
    days = int(input("Enter number of days on campus: "))

    # Get other weekly expenses (whole naira - int)
    other_expenses = int(input("Enter other expenses for the week (NGN): "))

    # Reject negative expense values or negative number of days
    if daily_transport < 0 or daily_feeding < 0 or other_expenses < 0 or days < 0:
        print("\nError: Negative values are not allowed for expenses or days.")
        print("Please run the program again with valid (non-negative) inputs.")
        return

    # Calculations
    transport_total = daily_transport * days
    feeding_total = daily_feeding * days
    weekly_total = transport_total + feeding_total + other_expenses

    # Display clear summary
    print("\nWEEKLY EXPENSE SUMMARY")
    print(f"Student: {student_name}")
    print(f"Transport total: NGN {transport_total:,}")
    print(f"Feeding total: NGN {feeding_total:,}")
    print(f"Other expenses: NGN {other_expenses:,}")
    print(f"Weekly total: NGN {weekly_total:,}")

    # Ask for weekly budget
    budget = int(input("\nEnter your weekly budget (NGN): "))

    # Reject negative budget
    if budget < 0:
        print("\nError: Negative budget is not allowed.")
        print("Please run the program again with a valid (non-negative) budget.")
        return

    # Compare expenses with budget
    print()  # blank line for readability
    if weekly_total < budget:
        remaining = budget - weekly_total
        print("Within budget")
        print(f"Amount remaining: NGN {remaining:,}")
    elif weekly_total == budget:
        print("Exactly on budget")
        print("Amount remaining: NGN 0")
    else:
        exceeded = weekly_total - budget
        print("Over budget")
        print(f"Amount exceeded: NGN {exceeded:,}")


if __name__ == "__main__":
    main()
