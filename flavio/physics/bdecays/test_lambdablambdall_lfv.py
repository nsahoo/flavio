import unittest
import numpy as np
import flavio


wc_sm = flavio.physics.eft.WilsonCoefficients()
wc_np = flavio.physics.eft.WilsonCoefficients()
wc_np.set_initial({'C10_bsemu':4., 'C10_bsmue':2.}, 160.)


class TestLb2LllLFV(unittest.TestCase):

    def test_lambdablambdall_lfv(self):

        obs_1 = flavio.classes.Observable["BR(Lambdab->Lambdaemu)"]
        obs_2 = flavio.classes.Observable["BR(Lambdab->Lambdamue)"]
        self.assertEqual(obs_1.prediction_central(flavio.default_parameters, wc_sm), 0)
        # BR(BR(Lambdab->Lambdaemu) should be 4 times larger as Wilson coeff is 2x the mue one                                                                                         
        self.assertAlmostEqual(
            obs_1.prediction_central(flavio.default_parameters, wc_np)
            /obs_2.prediction_central(flavio.default_parameters, wc_np),
            4.,  places=10)
        # test for errors                                                                                                                                                                             
        self.assertEqual(flavio.sm_prediction('BR(Lambdab->Lambdaemu)'), 0)
        self.assertEqual(flavio.sm_prediction('BR(Lambdab->Lambdamue)'), 0)


