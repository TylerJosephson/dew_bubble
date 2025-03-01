def antoine( a, T):
"""Antoine's equation calculator
    This uses Antoine's equation to calculate the vapor pressure of a fluid
    given the coefficients of the equation: Ps = a1 - a2/(a3 + T).

    Parameters
    ----------
    a : the Antoine coefficients with coefficients in columns and species in rows.
    T : the temperature to evaluate the vapor pressure at.
    
    Returns
    -------
    Ps : row vector of vapor pressures for all species at the specified temperature
    The units depend on the units used for the coefficients.  The user is
    responsible for maintaining consistency with units.  Customarily,
    coefficients are supplied for pressure in mmHg and T in Celsius. 
    
    The coefficient argument 'a' can be in typical Python list notation. 
    
    Examples
    --------
    >>> Ps = antoine(a, T)
    
    """
   import numpy as np
    a = np.array(a)
    b = np.shape(a)

    if len(b)==1:
        Ps = 10**(a[0]-a[1] / (a[2] + T) )
        Ps = np.round(Ps,3)
    else:
        Ps = 10.0**(a[:,0]-a[:,1] / ( a[:,2] + T ) )
        Ps = np.round(Ps,3)

    return Ps
