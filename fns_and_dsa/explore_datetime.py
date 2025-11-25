from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Show current date and time
    display_current_datetime()

    # Ask user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Calculate future date
    calculate_future_date(days)

if __name__ == "__main__":
    main()
