import datetime as dt

def display_current_datetime():
    current_datetime = dt.datetime.now()
    formatted_current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_datetime}")
    return current_datetime  # return the actual datetime object


def calculate_future_date():
    current_datetime = display_current_datetime()

    no_of_days = int(input("Enter the number of days to add to the current date: "))
    delta = dt.timedelta(days=no_of_days)

    future_date_only = current_datetime + delta

    future_date = future_date_only.date()    # write only the date part

    print(f"Future date: {future_date}")
    return future_date_only   # or return future_datetime if you want date + time

calculate_future_date()

    
