from datetime import date, timedelta

def display_current_datetime():
    current_datetime = date.today()
    formatted_current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_datetime}")
    return current_datetime  # return the actual datetime object


def calculate_future_date():
    current_datetime = display_current_datetime()

    no_of_days = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=no_of_days)

    future_date = current_datetime + delta

    print(f"Future date: {future_date}")

calculate_future_date()

    
