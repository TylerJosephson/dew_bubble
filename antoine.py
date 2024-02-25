def antoine( A, B, C, T):
    # Psat = antoine( A, B, C, T)
    #
    # Uses Antoine's equation to obtain the vapor pressure of a substance given
    # the coefficients of the equation:
    #  log(Psat) = A - B/(C+T)
    #
    # INPUTS:
    #  A, B, C - the antoine coefficients with coeffients in columns and species in
    #      rows. Coefficients units of bar and K.
    #  T - the temperature at which the vapor pressure is evaluated (K)
    #
    # OUTPUT:
    #  Psat - row vector of species vapor pressures at the specified temperature, in bar.
    #
    # The units depend on the units used for the coefficients. The user is
    # responsible for maintaining consistency with units. NIST uses bar and K.
    #
    # Code originally by: James C. Sutherland
    # Modified by: Tyler R. Josephson
    # Changed comment
    
    Psat = 10.0**( A[:] - B[:] / ( C[:] + T ) )
    return Psat
