# Distributed under the MIT License.
# See LICENSE for details.

from context import spheal

import numpy as np
import unittest

import spheal.radial as radial


class TestRadial(unittest.TestCase):
    """
    Test functions in `radial` module.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(2, 10)

        def test(profile, n_expected, r90_expected):
            r = np.random.rand(N)
            n = profile.number_fraction(r)
            self.assertTrue(
                np.allclose(n, n_expected(r)),
                msg=
                "partial number density for {profile} not giving expected result. "
                "RNG seed: {seed}.".format(profile="Exponential", seed=seed))

            self.assertTrue(
                np.allclose(profile.r90, r90_expected),
                msg="R_90 for {profile} not giving expected result. "
                "RNG seed: {seed}.".format(profile="Exponential", seed=seed))

        test(radial.Exponential(), lambda r: 1.0 - np.exp(-2.0 * r) *
             (1.0 + 2.0 * r + 2.0 * r**2), 2.661)


if __name__ == "__main__":
    unittest.main()
