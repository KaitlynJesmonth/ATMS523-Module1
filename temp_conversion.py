# This code can convert temperature between degrees Celsius and Kelvin.
# The output can be rounded to a specific number of decimal places.


def temp_conversion(temp, unit):
    """Calculates and returns the converted temperature from degrees Celsius to Kelvin or vice versa."""
    if unit == "C":
        temp_in = temp
        temp_out = temp_in + 273.15
        round_in = input("Would you like to round your answer? Type yes or no: ")
        if round_in == "yes":
            decimal_places = int(input("How many decimal places? "))
            temp_out = round(temp_out, decimal_places)
        return (str(temp_out) + " K")
    
    if unit == "K":
        temp_in = temp
        temp_out = temp_in - 273.15
        round_in = input("Would you like to round your answer? Type yes or no: ")
        if round_in == "yes":
            decimal_places = int(input("How many decimal places? "))
            temp_out = round(temp_out, decimal_places)
        return (str(temp_out)+" degrees C")


unit = input("Which unit would you like to input?\n"
             "Type C for degrees Celsius or K for Kelvin: ")
# Depending on the unit, give a descriptive input prompt.
if unit == "C":
    temp = float(input("Type a temperature to convert to Kelvin: "))
if unit == "K":
    temp = float(input("Type a temperature to convert to degrees Celsius: "))
output = temp_conversion(temp, unit)
print("Your converted temperature is", output)
    