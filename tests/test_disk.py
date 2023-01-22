# Distributed under the MIT License.
# See LICENSE for details.

import unittest

from context import spheal

import numpy as np

from spheal.disk import Disk


class TestDisk(unittest.TestCase):
    """
    Test `Disk` class.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        # Test properties of random tesselation.
        radius = np.random.rand()
        n_patches = np.random.randint(10, 100)

        # Choose random healthy patch aspect ratio.
        patch_aspect = np.random.rand()
        while (patch_aspect > 4. or patch_aspect < 0.5):
            patch_aspect = np.random.rand()

        disk = Disk(radius, n_patches, patch_aspect, draw=False)

        # Check that exactly `n_patches` patches have been created.
        self.assertEqual(disk.patch_number,
                         n_patches,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="patch number", seed=seed))

        # Check that the area of all inner circles equals area of outer circle.
        area = np.pi * radius**2.0 / n_patches
        number_sub = n_patches
        for annulus in disk.annuli:
            radius_sub = annulus.extents[1]
            area_sub = np.pi * radius_sub**2. / number_sub
            number_sub -= annulus.patch_number
            self.assertAlmostEqual(
                area,
                area_sub,
                msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                    f="area within r = {}".format(str(radius_sub)), seed=seed))

        def get_partial_numbers(disk):
            patch_numbers = []
            partial_number = 0
            for annulus in sorted(disk.annuli):
                partial_number += annulus.patch_number
                patch_numbers.append(partial_number)
            return patch_numbers

        # Get Beckers & Beckers 2012, Table 2, line 1. Also Table 5: Disk.
        disk_table_2 = Disk(radius=1., n_patches=288, patch_aspect=1.)
        self.assertEqual(get_partial_numbers(disk_table_2),
                         [1, 8, 21, 40, 66, 98, 136, 180, 231, 288],
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="comparison with BB12 Table 2", seed=seed))

        # Get Beckers & Beckers 2012, Table 4.
        disk_table_4 = Disk(radius=1., n_patches=1000, patch_aspect=1.)
        self.assertEqual(get_partial_numbers(disk_table_4), [
            1, 10, 25, 46, 73, 107, 147, 193, 245, 304, 369, 440, 518, 602,
            692, 788, 891, 1000
        ],
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="comparison with BB12 Table 4", seed=seed))


if __name__ == "__main__":
    unittest.main()
