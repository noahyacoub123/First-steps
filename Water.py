cas_number = "7732-18-5" #Values representing various constants, but only Tm and Tb will be used
rho = 1000
mu = 1
Tm = 273.15 #Kelvin measure of 0 degrees Celsius
Tb = 373.15 #Kelvin measure of 100 degrees Celsius
k = 0.58


def convert_to_kelvin(temperature, units): #First function converts either celsius or Fahrenheit or kelvin, based off of two inputs
    if type(temperature) not in [int, float]: #Just checking if types are valid
        return None
    if units not in ["F", "C"]:
        return None
    else:
        if units == "C": #Conversion for Celsius
            celc = temperature + Tm
            return celc
        if units == "F": #Conversion for Fahrenheit
            fara = ((temperature - 32) * (5 / 9)) + Tm
            return fara


def is_gas(temperature): #Second function checks if the temperature of water provided would result in a gas or not
    if type(temperature) not in [int, float]:
        return None
    else:
        if temperature > 373.15:
            return True
        else:
            return False


def is_liquid(temperature): #Third function checks if the temperature of water provided would result in a liquid or not
    if type(temperature) not in [int, float]:
        return None
    else:
        if 273.15 < temperature < 373.15:
            return True
        else:
            return False


def is_solid(temperature): #Final function checks if the temperature of water provided would result in a solid or not
    if type(temperature) not in [int, float]:
        return None
    else:
        if temperature < 273.15:
            return True
        else:
            return False


if __name__ == "__main__": #If the module is called instead of just imported, prompts the user for a unit and temperature measure and returns the state of water based off of that

    units = input("Units? ")
    temper = input("Temp? ")
    if temper.isnumeric(): #Checking that temperature value is given as a number, since inputs default to a string value
        temper1 = float(temper)

        kelvin = convert_to_kelvin(temper1, units)
        is_gas(kelvin)
        is_liquid(kelvin)
        is_solid(kelvin) #Calling all previous functions about the states of water

        if kelvin == None: #Checking that a value was actually given, if not, tells the user of the invalid input
            print("Invalid input!")
        else:

            if is_gas(kelvin) == True:
                print("gas")
            if is_liquid(kelvin) == True:
                print("liquid")
            if is_solid(kelvin) == True:
                print("solid")
            #Prints the state of water based off of the temperature given

    else:
        print("Invalid input!") #If a temperature value is given but it is not a numeric value, tells the user the input is unvalid