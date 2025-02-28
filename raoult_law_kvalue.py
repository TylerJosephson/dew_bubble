from antoine import antoine
import numpy as np

def raoult_law_kvalue( T, P, a, *gamma):
    # Calculates the equilibrium coefficient from Raoult's law
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
    #  Example: (eg: raoult_law_kvalue(500, 2, [1,2,3], *gamma))        
    #  
    # Code originally by James C. Sutherland
    # Modified by Tyler R. Josephson
    
    ns,nc = a.shape
    # makes np array of zeros
    K = np.zeros(ns) 
    Ps = antoine(a, T)  
    K = Ps/P
    if gamma = 1:
        print('The mixture is ideal')
    else
       print('The mixture is not ideal') 
        K *= gamma
    return K

