import numpy as np
def antoine( a, T):
    """    
        Ps = antoine( a, T)
        
        Uses Antoine's equation to obtain the vapor pressure of a substance given
        the coefficients of the equation:
        Ps = a1 - a2/(a3+T)
        
        INPUTS:
            a - the antoine coefficients with coeffients in columns and species in
                rows. Coefficients from NIST expect units of bar and K. A single row
                is also a valid input.
            T - the temperature at which the vapor pressure is evaluated (K)
                tempUnit - OPTIONAL the unit of temperature used
        
        OUTPUT:
            Ps - row vector of species vapor pressures at the specified temperature,
                typically in bar.
        
        The units depend on the units used for the coefficients. The user is
        responsible for maintaining consistency with units. NIST uses bar and K.

        Code originally by: James C. Sutherland
        Modified by: Tyler R. Josephson
    """
    #attempts to perform antoine equation calculation given input.
    try:
        #ensures input 'a' is an numpy array
        #note: applying np.array() to a numpy array does not modify the input
        #so there is no danger in performing this calculation for all 'a' input.
        a = np.array(a)

        #checks the number of dimensions in the 'a' array and performs
        #the appropriate form of the calculation.
        if a.ndim == 1:
            Ps = 10.0**( a[0] - a[1] / ( a[2] + T ) )
        elif a.ndim == 2:
            Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T ) )
        else:
            Ps = 'a'
        Ps/1.0
    except TypeError:
        print("Invalid array type. Must be 1-d or 2-d as in docstring.")
    return Ps