# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Zone:
    """
    The surface of a spherical segment (excluding the bases).
    """

    def __init__(self, extents: list, n_patches: int):
        self._extents = extents
        self._patch_extents = [
            2.0 * np.pi * m / n_patches for m in range(n_patches + 1)
        ]

    @property
    def extents(self) -> list:
        """
        The zenithal coordinates defining the zone.
        """
        return self._extents

    @property
    def patch_extents(self) -> list:
        """
        The azimuthal extents of the patches that constitute the zone. The zone
        is divided into equal-shape patches.
        """
        return self._patch_extents
