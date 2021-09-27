def antoine( a, T ):
    # More text in the comments
    # Ps = antoine( a, T )
    #
    # Uses Antoine's equation to obtain the vapor pressure of a substance given
    # the coefficients of the equation:
    #  Ps = a1 - a2/(a3+T)
    #
    # INPUTS:
    #  a - the antoine coefficients with coeffients in columns and species in
    #      rows. Coefficients from NIST expect units of bar and K.
    #  T - the temperature at which the vapor pressure is evaluated (K)
    #
    # OUTPUT:
    #  Ps - row vector of species vapor pressures at the specified temperature,
    #       typically in bar.
    #
    # The units depend on the units used for the coefficients. The user is
    # responsible for maintaining consistency with units. NIST uses bar and K.
    #
    # Code originally by: James C. Sutherland
    # Modified by: Tyler R. Josephson

    Ps = 10.0**( a[:,0] - a[:,1] / ( a[:,2] + T ) )
    return Ps
