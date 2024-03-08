import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import unittest
import numpy as np
import antoine as antoine
import raoult_law_kvalue as rlk
import get_antoine_coefficient as gac

class Testsrc(unittest.TestCase):

    #test 1
    def test_antoine_01(self):
        a = [6.80398, 803.810,  246.990] #Kelvin, bar
        T = 300 #Kelvin
        self.assertAlmostEqual(antoine.antoine(a, T),  216005.60373829)
    
    #test 2
    def test_antoine_02(self):
        a = np.array([6.80398, 803.810,  246.990]) #Kelvin, bar
        T = 300 #Kelvin
        self.assertAlmostEqual(antoine.antoine(a, T),  216005.60373829)

    #test 3
    def test_antoine_03(self):
        propane = [6.80398, 803.810,  246.990]
        benzene = [6.90565, 1211.033, 220.79 ]
        antoineCoefs = np.array( [propane, benzene] )
        T = 300
        self.assertEqual(antoine.antoine(antoineCoefs, T).all(),  np.array([216005.60373829,  38042.86084146]).all())

    #test 4
    def test_antoine_04(self):
        propane = [6.80398, 803.810,  246.990]
        benzene = [6.90565, 1211.033, 220.79 ]
        antoineCoefs = np.array( [propane, benzene] )
        T = [300]
        self.assertEqual(antoine.antoine(antoineCoefs, T).all(),  np.array([216005.60373829,  38042.86084146]).all())

    #test 5
    def test_raoult_01(self):
        from scipy.optimize import newton

        P = 101325  #Pressure in Pa
        #We should update this example! Units of test not consistent with NIST
        propane = [6.80398, 803.810,  246.990]
        benzene = [6.90565, 1211.033, 220.79 ]
        antoineCoefs = np.array( [propane, benzene] )

        z = 0.5

        def resfun_bubble( T ):
            return 1 - np.sum( z * rlk.raoult_law_kvalue(T,P,antoineCoefs) )
        Tb = newton(resfun_bubble,300)
        self.assertAlmostEqual(Tb, 268.527069352912)

    #test 6
    def test_raoult_02(self):
        from scipy.optimize import newton
        P = 101325  #Pressure in Pa
        #We should update this example! Units of test not consistent with NIST
        propane = [6.80398, 803.810,  246.990]
        benzene = [6.90565, 1211.033, 220.79 ]
        antoineCoefs = np.array( [propane, benzene] )

        z = 0.5
        def resfun_dew( T ):
            return 1 - np.sum( z / rlk.raoult_law_kvalue(T,P,antoineCoefs) )

        Td = newton(resfun_dew,   300)
        self.assertAlmostEqual(Td, 351.22607054163893)

    #test 7
    def test_get_antoine_coefficient_01(self):
        pcoeffs = gac.get_antoine_coefficient('propane', 300)
        trueresult = [4.53678, 1149.36, 24.906, 277.6, 360.8]
        self.assertListEqual(pcoeffs, trueresult)

    #test 8
    def test_get_antoine_coefficient_02(self):
        import io
        # create a trap using neat method from https://codingdose.info/posts/supress-print-output-in-python/
        text_trap = io.StringIO()
        sys.stdout = text_trap

        pcoeffs = gac.get_antoine_coefficient('propane', 150)

        # restore stdout
        sys.stdout = sys.__stdout__


        trueresult = None
        self.assertEqual(pcoeffs, trueresult)





if __name__ == '__main__':
    unittest.main(verbosity=2)