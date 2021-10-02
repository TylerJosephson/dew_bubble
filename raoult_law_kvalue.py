from antoine import antoine
import numpy as np

def raoult_law_kvalue( T, P, a, tempUnit="K", *gamma):
    # Calculates the equilibrium coefficient from Raoult's law
    # Change on line 6
    # INPUTS:
    #
    #  T - temperature (units of K)
    #
    #  P - pressure (units of bar)
    #
    #  a - Antoine equation coefficients with coefficients for each species in
    #      a row. When drawing Antoine coefficients from NIST, these will expect T
    #      and p in units of K and bar. Antoine coefficients from other sources 
    #      will require compatible units.
    #
    #  tempUnit - OPTIONAL the unit of temperature used
    #
    #  gamma - OPTIONAL activity coefficients for use in a modified Raoult's law.
    #
    #  tempUnit - The units of temperature. Can be Kelvin, Fahrenheit, Celsius, or Rankine
    #             Parameter should be inputted as the first letter of the temperature scale.
    #             
    #
    # OUTPUT:
    #
    #  K - row vector containing the K-value for each species
    #
    #  Example: (eg: raoult_law_kvalue(500, 2, [1,2,3], *gamma, F))        
    #  
    # Code originally by James C. Sutherland
    # Modified by Tyler R. Josephson
    
    ns,nc = a.shape
    
    K = np.zeros(ns)
    Ps = antoine(a, T, tempUnit)  
    K = Ps/P
    if gamma:
        K *= gamma

    return K



# This is intended to test things to ensure that it is working properly.
if __name__ == '__main__':
    from scipy.optimize import newton

    P = 101325  # Pressure in Pa

    # We should update this example! Units of test not consistent with NIST
    propane = [6.80398, 803.810,  246.990]
    benzene = [6.90565, 1211.033, 220.79 ]
    antoineCoefs = np.array( [propane, benzene] )

    z = 0.5

    def resfun_bubble( T ):
        return 1 - np.sum( z * raoult_law_kvalue(T,P,antoineCoefs) )

    def resfun_dew( T ):
        return 1 - np.sum( z / raoult_law_kvalue(T,P,antoineCoefs) )

    Tb = newton(resfun_bubble,300)
    Td = newton(resfun_dew,   300)

    if abs( Tb - 248 ) > 0.2:
        print('FAILED.  Expected bubble point temperature of 248.0 but found {:.1f}'.format(Tb))
    if abs( Td - 333.0 ) > 0.2:
        print('FAILED.  Expected dew point temperature of 333.0 but found {:.1f}'.format(Td))


    print('\n\t-> Bubble point: {:.1f} K\n\t-> Dew    point: {:.1f} K'.format(Tb,Td))
