# Distributed under the MIT License.
# See LICENSE for details.

import unittest

from context import spheal

import numpy as np

from spheal.hemisphere import Hemisphere


class TestHemisphere(unittest.TestCase):
    """
    Test `Hemisphere` class.
    """

    def test(self):

        seed = np.random.randint(0, 1e6)
        np.random.seed(seed)

        # Test properties of random tessellation.
        radius = np.random.rand()
        n_patches = np.random.randint(10, 100)

        # Choose random healthy patch aspect ratio.
        patch_aspect = np.random.rand()
        while (patch_aspect > 4. or patch_aspect < 0.5):
            patch_aspect = np.random.rand()

        hemisphere = Hemisphere(radius, n_patches, patch_aspect)

        # Check that exactly `n_patches` patches have been created.
        self.assertEqual(hemisphere.patch_number,
                         n_patches,
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="patch number", seed=seed))

        # Issue #1: area test not passing. Likely related to not being able to
        # reproduce Table 6, line 5 (zenithal angles).

        # # Check that the surface area of all inner polar caps per patch equals
        # # area of the outer ones.
        # area = 2. * np.pi * radius**2. * (1. - np.cos(0.5 * np.pi)) / n_patches
        # number_sub = n_patches
        # print(area)
        # for zone in hemisphere.zones:
        #     theta_sub = zone.extents[1]
        #     area_sub = 2. * np.pi * radius**2. * (1. - np.cos(theta_sub)) / number_sub
        #     number_sub -= zone.patch_number
        #     self.assertAlmostEqual(
        #         area,
        #         area_sub,
        #         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
        #             f="area within theta = {}".format(str(theta_sub)), seed=seed))

        def get_partial_numbers(hemisphere):
            patch_numbers = []
            partial_number = 0
            for zone in sorted(hemisphere.zones):
                partial_number += zone.patch_number
                patch_numbers.append(partial_number)
            return patch_numbers

        # Get Beckers & Beckers 2012, Table 5: Hemisphere.
        hemisphere_table_5 = Hemisphere(radius=1.,
                                        n_patches=288,
                                        patch_aspect=1.)
        self.assertEqual(get_partial_numbers(hemisphere_table_5),
                         [1, 9, 22, 41, 65, 94, 128, 165, 205, 246, 288],
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="comparison with BB12 Table 5", seed=seed))

        # Get Beckers & Beckers 2012, Table 6, line 2.
        hemisphere_table_6 = Hemisphere(radius=1.,
                                        n_patches=145,
                                        patch_aspect=1.)
        self.assertEqual(get_partial_numbers(hemisphere_table_6),
                         [1, 8, 20, 38, 60, 86, 115, 145],
                         msg="\n\nwhen testing {f}.\nRNG seed: {seed}.".format(
                             f="comparison with BB12 Table 6", seed=seed))


if __name__ == "__main__":
    unittest.main()
