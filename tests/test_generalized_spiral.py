# Distributed under the MIT License.
# See LICENSE for details.

from context import sphrdis

import numpy as np
import unittest

from sphrdis.generalized_spiral import GeneralizedSpiral


class TestGeneralizedSpiral(unittest.TestCase):
    """
    Test functions in `GeneralizedSpiral` class.
    """

    @staticmethod
    def name():
        return "TestGeneralizedSpiral"

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(4, 10)
        dis = GeneralizedSpiral(N)

        self.assertTrue(
            N == dis.N,
            msg="In {name}: class member N differs from expected value. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        some_k = np.random.randint(2, N - 1)
        hk = dis._h(some_k)
        hk_expected = -1.0 + 2.0 * (some_k - 1.0) / (N - 1.0)
        self.assertTrue(
            np.allclose(hk, hk_expected),
            msg="In {name}: result of h_k differs from expected value. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        phase = dis._phase(hk)
        phase_expected = 3.6 / np.sqrt(N * (1.0 - hk**2))
        self.assertTrue(
            np.allclose(phase, phase_expected),
            msg="In {name}: result of phase differs from expected value. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        theta_expected = np.empty(N)
        for k in range(0, N):
            theta_expected[k] = np.arccos(dis._h(k + 1))

        phi_expected = np.zeros(N)
        for k in range(1, N - 1):
            phi_expected[k] = phi_expected[k - 1] + dis._phase(dis._h(k + 1))

        self.assertTrue(
            np.allclose(dis.theta, theta_expected),
            msg="In {name}: member theta differs from expected value. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        self.assertTrue(
            np.allclose(dis.phi, phi_expected),
            msg="In {name}: member phi differs from expected value. "
            "RNG seed: {seed}.".format(name=self.name(), seed=seed))

        print("\nAll tests in {s} passed.".format(s=self.name()))


if __name__ == "__main__":
    unittest.main()
