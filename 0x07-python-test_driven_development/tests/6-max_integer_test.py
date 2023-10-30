"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class for the Unit test of max_integer function."""

    def test_empty(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer(), None)

    def test_none(self):
        """Unit test for max_integer function."""
        self.assertEqual(None, None)

    def test_same_elements(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([10, 10, 10, 10, 10]), 10)

    def test_negative(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([-1, -10000, -1242]), -1)

    def test_ascending_order(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_descending_order(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_unordered(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_pos_neg(self):
        """Unit test for max_integer function."""
        self.assertEqual(max_integer([0, -10, 10, -102, 93, 99]), 99)

    def test_large_neg(self):
        """Unit test for max_integer function."""
        self.assertEqual(
                max_integer([-34597, -61152, -35387, -19133,
                            -75800, -89975, -97128, -72671, -11321, -28505,
                            -41475, -78147, -73106, -69404, -58887, -33282,
                            -36652, -59682, -85368, -96267, -33856, -48872,
                            -17997, -27658, -54368, -30424, -97206, -38289,
                            -81859, -22808, -25884, -5212, -31089, -12592,
                            -99430, -75855, -62252, -99131,
                            -49896, -33970]), -5212)

    def test_large_pos(self):
        """Unit test for max_integer function."""
        self.assertEqual(
                max_integer([130087, 875428, 535437, 789772,
                            542533, 861633, 370237, 705691,
                            488470, 755327, 60447, 47734, 591726,
                            17358, 601660, 4913, 611011, 859077,
                            876338, 300300, 729083, 712429, 866244,
                            385227, 605392, 45726, 93632, 959882,
                            667626, 233482, 10846, 232524, 815026,
                            846674, 179889, 435355, 811260, 652629,
                            894133, 212890]), 959882)

    def test_large_neg_pos(self):
        """Unit test for max_integer function."""
        self.assertEqual(
                max_integer([-420272, 870835, -51028, 233165, 125719,
                            864282, 68815, 873080, -111572, -874046, 301194,
                            772800, -768152, -287089, -241179, -425426,
                            -786546, 360031, 367809, -209260, 197625,
                            -364045, -455076, -695042, -777240, -684814,
                            273262, -381280, -890189, -69618, -743492,
                            -783451, -706755, 18493, -434797, 525945,
                            288890, -319734, 343095, -948022]), 873080)

    def test_pos_floats(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([7015282.606173002, 6243999.896637975,
                        284517.73743712436, 7273964.597579881,
                        33432.50470755788, 7024448.511155016,
                        5787690.0744613735, 5614807.811428043,
                        1741721.683740184, 8973547.937826814,
                        6000551.200176802, 3792886.1172510698,
                        6419933.278682376, 5868111.286620203,
                        5125693.888455908, 8676136.90812898,
                        7005775.858457052, 5035399.05941626,
                        4398407.307639004, 6810180.697404385,
                        6292845.120713888, 7458672.677703967,
                        5104378.63525028, 7182101.126995986,
                        933887.2283219313, 8908090.317776872,
                        2404031.311527064, 2774356.772023504,
                        1701758.6311974165, 9807718.687694931,
                        5734582.490298441, 6054445.079190611,
                        8711713.087525913, 2765096.361374488,
                        7787102.889068262, 8785445.988192935,
                        332478.9458222788, 4103018.6930257706,
                        3866393.4491523635,
                        1311227.8370308417]), 9807718.687694931)

    def test_neg_floats(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([-5318343.776809619, -4394026.286833531,
                        -4075261.028855852, -1637923.8469319493,
                        -681657.01644429, -4592069.238097125,
                        -5347423.189086641, -1984365.4958671965,
                        -5690846.612442112, -5470774.882598212,
                        -3676225.268465489, -1976595.2249262147,
                        -5296952.80040282, -3249775.9380921694,
                        -4295347.6892812215, -5340516.670165288,
                        -3243177.624657199, -6256777.326642748,
                        -208777.17335879616, -8483473.16653426,
                        -1022540.3928242549, -8581255.900149297,
                        -2892692.6376400674, -5277923.878530115,
                        -5121888.576302588, -6481739.605478363,
                        -406704.91848009266, -235611.8622336462,
                        -5347787.349443933, -1776840.2362328665,
                        -4684177.092580601, -3489560.0165237766,
                        -783052.3443387579, -8458767.435929433,
                        -2210055.1438702075, -6874928.384942289,
                        -463798.1439804081, -5424297.725403352,
                        -8626252.57420813,
                        -8645057.536142811]), -208777.17335879616)

    def test_neg_pos_floats(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([-4710032.943517595, 6847801.492137492,
                        -5797322.7731864555, 3054782.8480709344,
                        1027063.2738052141, 5405351.798899973,
                        5519096.019863993, -2358221.62150749,
                        2344592.2420237716, 335998.0047811158,
                        838990.3349243216, 4832622.866072284,
                        3067522.168469455, -6794732.346315982,
                        2900877.5201990325, 5869747.30538547,
                        5828279.628716525, -2291291.289603605,
                        2103437.180619072, -6892450.006542416,
                        2268851.275292963, 2287493.9735949095,
                        3150171.888583366, 9136855.372901544,
                        -8758503.064170431, 4766022.676553231,
                        2018290.6676861197, 7721408.880781576,
                        -8060985.245371521, 4996634.080010286,
                        3753481.201275401, 256973.32608873583,
                        -527305.3986359946, -3437777.3789554182,
                        7650164.252457626, -4059846.750928211,
                        -6396942.981569065, -5854896.127540087,
                        -574071.0421530474,
                        -1491288.6867206488]), 9136855.372901544)

    def test_int_float(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([10, -10.1, 0, 0.1, 8, 10.001,
                        -173.32, -12.0]), 10.001)

    def test_infinity(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([10, -10.1, float("-inf"), 0.1,
                        17, float("inf"), -173.32, -12.0]), float("inf"))

    def test_nan(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([10, -10.1, float("nan"), 0.1,
                        17, float("nan"), -173.32, -12.0]), 17)

    def test_string(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer("yousef ayman"), "y")

    def test_numeric_string(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer("218468214276252735"), "8")

    def test_lists(self):
        """Unit test for max_integer function."""
        self.assertEqual(
            max_integer([[], [1], [9], [1, 10]]), [9])

    def test_mixed_list(self):
        """Unit test for max_integer function."""
        with self.assertRaises(TypeError):
            max_integer([100, "s", None, 10.1, True, [12]])

    def test_int(self):
        """Unit test for max_integer function."""
        with self.assertRaises(TypeError):
            max_integer(69)

    def test_float(self):
        """Unit test for max_integer function."""
        with self.assertRaises(TypeError):
            max_integer(45.134)

    def test_dict(self):
        """Unit test for max_integer function."""
        with self.assertRaises(TypeError):
            max_integer([{1: 2, 3: 4}, {"as": "db"}, {True: False}])


if __name__ == "__main__":
    unittest.main()
