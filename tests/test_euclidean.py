# Distributed under the MIT License.
# See LICENSE for details.

from context import spheal

import numpy as np
import unittest

import spheal.euclidean as euclidean


class TestCartesianFromSpherical(unittest.TestCase):
    """
    Test `spherical_from_cartesian` function.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(4, 10)

        rad = np.random.rand(N)
        the = np.random.rand(N)
        phi = np.random.rand(N)

        coords = np.empty((N, 3))

        euclidean.cartesian_from_spherical(coords, rad, the, phi)

        coords_expected = np.empty((N, 3))
        for k in range(N):
            coords_expected[k, 0] = rad[k] * np.sin(the[k]) * np.cos(phi[k])
            coords_expected[k, 1] = rad[k] * np.sin(the[k]) * np.sin(phi[k])
            coords_expected[k, 2] = rad[k] * np.cos(the[k])

        self.assertTrue(
            np.allclose(coords, coords_expected),
            msg="cartesian_from_spherical not giving expected result. "
            "RNG seed: {seed}.".format(seed=seed))


class TestRotateAbout(unittest.TestCase):
    """
    Test `rotate_about` function.
    """

    def test(self):
        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        angle = np.random.randn()
        k = np.random.randn(3)
        k = k / np.sqrt(np.dot(k, k))

        v = np.array([0.0, 1.0, 0.0])
        v_copy = v.copy()
        euclidean.rotate_about(v, k, angle)

        v_expected = np.cos(angle) * v_copy + np.cross(k, v_copy) * np.sin(
            angle) + k * np.dot(k, v_copy) * (1.0 - np.cos(angle))

        self.assertTrue(np.allclose(v, v_expected),
                        msg="rotate_about not giving expected result. "
                        "RNG seed: {seed}.".format(seed=seed))


if __name__ == "__main__":
    unittest.main()
