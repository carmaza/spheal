# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Annulus:
    """
    The 2-d region between two concentric circles.
    """

    def __init__(self, extents: tuple, n_patches: int):
        self._extents = extents
        self._patch_extents = tuple(2.0 * np.pi * m / n_patches
                                    for m in range(n_patches + 1))

    @property
    def extents(self) -> tuple:
        """
        The radial extents of the annulus.
        """
        return self._extents

    @property
    def patch_extents(self) -> tuple:
        """
        The angualr extents of the patches that constitute the annulus.
        The annulus is divided into equal-shape patches.
        """
        return self._patch_extents
