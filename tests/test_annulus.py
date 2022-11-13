# Distributed under the MIT License.
# See LICENSE for details.

from context import sphrdis

import numpy as np
import unittest

from sphrdis.annulus import Annulus


class TestAnnulus(unittest.TestCase):
    """
    Test `Annulus` class.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        n_patches = np.random.randint(2, 10)
        extents = tuple(sorted(np.pi * np.random.rand(2)))

        annulus = Annulus(extents, n_patches)
        self.assertEqual(annulus.extents,
                         extents,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="extents", seed=seed))
        self.assertEqual(tuple(2.0 * np.pi * m / n_patches
                               for m in range(n_patches + 1)),
                         annulus.patch_extents,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="patch extents", seed=seed))


if __name__ == "__main__":
    unittest.main()