FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (user_prompt - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = user_prompt * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

prompt = input("Enter the temperature to convert: ")
prompt1 = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
try:
    user_prompt = float(prompt)
    if prompt1 == "F":
        result = convert_to_celsius(user_prompt)
        print(f"{user_prompt}\u00B0F is {result}\u00B0C")

    elif prompt1 == "C":
        result = convert_to_fahrenheit(user_prompt)
        print(f"{user_prompt}\u00B0C is {result}\u00B0F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
