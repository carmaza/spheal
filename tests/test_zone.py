# Distributed under the MIT License.
# See LICENSE for details.

from context import spheal

import numpy as np
import unittest

from spheal.zone import Zone


class TestZone(unittest.TestCase):
    """
    Test `Zone` class.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        n_patches = np.random.randint(2, 10)
        extents = tuple(sorted(np.pi * np.random.rand(2)))

        zone = Zone(extents, n_patches)
        self.assertEqual(zone.extents,
                         extents,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="extents", seed=seed))
        self.assertEqual(zone.patch_number,
                         n_patches,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="patch number", seed=seed))
        self.assertEqual(tuple(2.0 * np.pi * m / n_patches
                               for m in range(n_patches + 1)),
                         zone.patch_extents,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="patch extents", seed=seed))

        self.assertTrue(Zone((0.4, 0.5), 10) > Zone((0.2, 0.4), 10),
                        msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                            f="< operator", seed=seed))


if __name__ == "__main__":
    unittest.main()
