def temp_converter(T, temp_unit):
    # temp_unit should be a string
    # K for kelvin scale, 
    # C for Celsius scale ,
    # F for Fahrenheit scale,
    # R for Rankine scale
    if temp_unit == 'K':
        return T
    elif temp_unit == 'C':
        return T + 273.15
    elif temp_unit == 'F':
        return (T + 459.67) * 5/9
    elif temp_unit == 'R':
        return T / 1.8
    else:
        return "Unit not supported"


def pressure_converter(P, pressure_unit):
    # pressure_unit should be a string
    if pressure_unit == 'bar':
        return P
    elif pressure_unit == 'pascal':
        return P / 100000
    elif pressure_unit == 'psi':
        return P / 14.504
    elif pressure_unit == 'mmHg':
        return P / 750
    elif pressure_unit == 'atm':
        return P * 1.013
    else:
        return "Unit not supported"

