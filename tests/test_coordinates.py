# Distributed under the MIT License.
# See LICENSE for details.

from context import sphrdis

import numpy as np
import unittest

import sphrdis.coordinates as coordinates


class TestCoordinates(unittest.TestCase):
    """
    Test functions in `coordinates` module.
    """

    @staticmethod
    def name():
        return "TestCoordinates"

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(4, 10)

        rad = np.random.rand(N)
        the = np.random.rand(N)
        phi = np.random.rand(N)

        coords = np.empty((N, 3))
        coordinates.cartesian_from_spherical(coords, rad, the, phi)

        coords_expected = np.empty((N, 3))
        for k in range(N):
            coords_expected[k, 0] = rad[k] * np.sin(the[k]) * np.cos(phi[k])
            coords_expected[k, 1] = rad[k] * np.sin(the[k]) * np.sin(phi[k])
            coords_expected[k, 2] = rad[k] * np.cos(the[k])

        self.assertTrue(
            np.allclose(coords, coords_expected),
            msg=
            "In {name}: cartesian_from_spherical not giving expected result. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        print("\nAll tests in {s} passed.".format(s=self.name()))


if __name__ == "__main__":
    unittest.main()
