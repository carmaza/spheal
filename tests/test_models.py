# Distributed under the MIT License.
# See LICENSE for details.

from context import sphrdis

import numpy as np
import unittest

import sphrdis.models as models


class TestModels(unittest.TestCase):
    """
    Test functions in `Models` module.
    """

    @staticmethod
    def name():
        return "TestModels"

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        N = np.random.randint(2, 10)

        def test(model, n_expected):
            r = np.random.rand(N)
            n = model.partial_number_density(r)
            self.assertTrue(
                np.allclose(n, n_expected(r)),
                msg=
                "In {name}: partial number density for {model} not giving expected result. "
                "RNG seed: {seed}.".format(name=self.name(),
                                           model="Exponential",
                                           seed=seed))

        test(models.Exponential(), lambda r: np.exp(-2.0 * r) *
             (1.0 + 2.0 * r + 2.0 * r**2))

        print("\nAll tests in {s} passed.".format(s=self.name()))


if __name__ == "__main__":
    unittest.main()
