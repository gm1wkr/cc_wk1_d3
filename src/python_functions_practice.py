def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(month):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Offset Index
    month -= 1

    return months[month]

def number_to_short_month_name(month):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]

    # Offset Index ??? Better way to do this is ??
    # month -= 1
    # return months[month]
    return months[month-1]

def volume_of_cube(length_of_side):
    return pow(length_of_side, 3)

def reverse_string(string_to_reverse):
    # string[start : stop : step]
    # https://stackoverflow.com/questions/509211/understanding-slicing
    return string_to_reverse[::-1]

def fahrenheit_to_celsius(fahrenheit):
    # rounded down 
    return round((fahrenheit - 32) * 5/9)