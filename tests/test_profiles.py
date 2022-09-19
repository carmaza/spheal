# Distributed under the MIT License.
# See LICENSE for details.

from context import sphrdis

import numpy as np
import unittest

import sphrdis.profiles as profiles


class TestProfiles(unittest.TestCase):
    """
    Test functions in `Profiles` module.
    """

    @staticmethod
    def name():
        return "TestProfiles"

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(2, 10)

        def test(profile, n_expected):
            r = np.random.rand(N)
            n = profile.partial_number_density(r)
            self.assertTrue(
                np.allclose(n, n_expected(r)),
                msg=
                "In {name}: partial number density for {profile} not giving expected result. "
                "RNG seed: {seed}.".format(name=self.name(),
                                           profile="Exponential",
                                           seed=seed))

        test(profiles.Exponential(), lambda r: np.exp(-2.0 * r) *
             (1.0 + 2.0 * r + 2.0 * r**2))

        print("\nAll tests in {s} passed.".format(s=self.name()))


if __name__ == "__main__":
    unittest.main()
