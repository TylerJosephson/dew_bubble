def antoine( a, T):
    # Ps = antoine( a, T)
    #
    # Uses Antoine's equation to obtain the vapor pressure of a substance given
    # the coefficients of the equation:
    #  Ps = a1 - a2/(a3+T)
    #
    # INPUTS:
    #  a - the antoine coefficients with coeffients in columns and species in
    #      rows. Coefficients from NIST expect units of bar and K.
    #  T - the temperature at which the vapor pressure is evaluated (K)
    #  tempUnit - OPTIONAL the unit of temperature used
    # If temperature is given with the units of farenheit an additional equation is needed to change the units of temperature 
    # This equation takes in the given temperature in units of farenheit and converts it to an output of temperature in the units of kelvin
    # To use the nist coeeficients temperature needs to be in kelvin 
    
    T_K = (32*T − 32) * (5/9) + 273 
    # OUTPUT:
    #  Ps - row vector of species vapor pressures at the specified temperature,
    #       typically in bar.
    #
    # The units depend on the units used for the coefficients. The user is
    # responsible for maintaining consistency with units. NIST uses bar and K.
    #
    # Code originally by: James C. Sutherland
    # Modified by: Tyler R. Josephson
    
    Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T_K ) )
    return Ps
