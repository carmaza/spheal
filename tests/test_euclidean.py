# Distributed under the MIT License.
# See LICENSE for details.

import unittest

import numpy as np

from spheal import euclidean


class TestCartesianFromSpherical(unittest.TestCase):
    """
    Test `cartesian_from_spherical` function.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(4, 10)

        r = np.random.rand(N)
        theta = np.random.rand(N)
        phi = np.random.rand(N)

        coords = np.empty((N, 3))

        euclidean.cartesian_from_spherical(coords, r, theta, phi)

        coords_expected = np.empty((N, 3))
        for k in range(N):
            coords_expected[k, 0] = r[k] * np.sin(theta[k]) * np.cos(phi[k])
            coords_expected[k, 1] = r[k] * np.sin(theta[k]) * np.sin(phi[k])
            coords_expected[k, 2] = r[k] * np.cos(theta[k])

        self.assertTrue(
            np.allclose(coords, coords_expected),
            msg="cartesian_from_spherical not giving expected result. "
            "RNG seed: {seed}.".format(seed=seed))


class TestSphericalFromCartesian(unittest.TestCase):
    """
    Test `spherical_from_cartesian` function.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(4, 10)

        x = np.random.rand(N)
        y = np.random.rand(N)
        z = np.random.rand(N)
        r = np.sqrt(x * x + y * y + z * z)

        theta, phi = np.empty_like(x), np.empty_like(x)
        euclidean.spherical_from_cartesian(theta, phi, x, y, z)

        theta_expected = np.arccos(z / r)
        self.assertTrue(
            np.allclose(theta, theta_expected),
            msg="spherical_from_cartesian theta not giving expected result. "
            "RNG seed: {seed}.".format(seed=seed))

        phi_expected = np.arctan2(y, x)
        self.assertTrue(
            np.allclose(phi, phi_expected),
            msg="spherical_from_cartesian phi not giving expected result. "
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
