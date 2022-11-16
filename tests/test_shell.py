# Distributed under the MIT License.
# See LICENSE for details.

from context import spheal

import numpy as np
import unittest

import spheal.shell as shell

from spheal.profiles import Exponential


class TestParticleNumber(unittest.TestCase):
    """
    Test `particle_number` function.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(100, 1000)
        nshells = np.random.randint(3, 10)

        numbers = np.empty(nshells, dtype=np.uint32)

        # Specific profile doesn't matter.
        profile = Exponential()
        r = np.array([0.1 * k for k in range(0, nshells + 1)])

        shell.particle_number(numbers, profile, N, r)

        f = profile.number_fraction(r)
        numbers_expected = np.empty(nshells, dtype=np.uint32)
        for j in range(0, nshells):
            numbers_expected[j] = np.rint(N * (f[j] - f[j + 1]))

        self.assertTrue(np.allclose(numbers, numbers_expected),
                        msg="shell numbers not giving expected result. "
                        "RNG seed: {seed}.".format(seed=seed))


if __name__ == "__main__":
    unittest.main()
