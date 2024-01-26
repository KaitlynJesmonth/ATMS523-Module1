# This code takes user input of Celsius and outputs Kelvin


def temp_conversion(t_degC):
    """Calculates and returns the converted temperature from degrees Celsius to Kelvin"""
    temp_in = t_degC
    temp_out = t_degC + 273.15
    return (str(temp_out)+" K")


def main():
    t_degC = float(input("Type a temperature in Celsius to convert to Kelvin: "))
    print(temp_conversion(t_degC))

if __name__ == "__main__":
    main()






    