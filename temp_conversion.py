# This code can convert temperature between degrees Celsius and Kelvin.


def temp_conversion(temp, unit):
    """Calculates and returns the converted temperature from degrees Celsius to Kelvin or vice versa."""
    if unit =="C":
        temp_in = temp
        temp_out = temp + 273.15
        return (str(temp_out)+" K")
    
    if unit=="K":
        temp_in = temp
        temp_out = temp - 273.15
        return (str(temp_out)+" degrees C")


unit = input("Which unit would you like to input?\n"
             "Type C for degrees Celsius or K for Kelvin: ")
# Depending on the unit, give a descriptive input phrase.
if unit=="C":
    temp = float(input("Type a temperature to convert to Kelvin: "))

if unit=="K":
    temp = float(input("Type a temperature to convert to degrees Celsius: "))
output = temp_conversion(temp, unit)
print("Your converted temperature is ", output)
    