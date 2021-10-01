def temp_converter(T):
    print("Choose the unit of your input temperature (1, 2, 3 or 4) ")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Rankine")
    print("4. Kelvin")
    temp_unit = float(input("temp selection: "))
    if temp_unit == 4:
        return T
    elif temp_unit == 1:
        return T + 273.15
    elif temp_unit == 2:
        return (T + 459.67) * 5/9
    elif temp_unit == 3:
        return T / 1.8
    else:
        return "Unit not supported"


def pressure_converter(P):
    print("Choose the unit of your input temperature (input 1, 2, 3, 4 or 5) ")
    print("1. pascal")
    print("2. psi")
    print("3. mm Hg")
    print("4. atm")
    print("5: bar")
    pressure_unit = float(input("pressure selection: "))
    
    if pressure_unit == 5:
        return P
    elif pressure_unit == 1:
        return P / 100000
    elif pressure_unit == 2:
        return P / 14.504
    elif pressure_unit == 3:
        return P / 750
    elif pressure_unit == 4:
        return P * 1.013
    else:
        return "Unit not supported"



