# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines class `Zone`.

"""

import numpy as np


class Zone:
    """
    The surface of a spherical segment (excluding the bases).

    This class represents a natural unit for the tessellation of a hemisphere
    consisting of cells whose boundaries are parallel and meridian arcs.

    Members
    -------

    `extents`: tuple
    The zenithal extents of the zone.

    `patch_number`: int
    The number of patches in the zone.

    `patch_extents`: tuple
    The azimuthal extents of the patches that constitute the zone.

    Notes
    -----

    - Each patch has exactly the same shape.

    """

    def __init__(self, extents: tuple, n_patches: int):
        """
        Parameters
        ----------

        `extents`: tuple
        A 2-d tuple containing the zenithal extents of the zone.

        `n_patches`: int
        The number of azimuthal patches into which to divide the zone.

        """
        self._extents = extents
        self._patch_extents = tuple(2.0 * np.pi * m / n_patches
                                    for m in range(n_patches + 1))

    def __lt__(self, other):
        return self.extents[0] < other.extents[0]

    @property
    def extents(self) -> tuple:
        """
        The radial extents of the zone.

        """
        return self._extents

    @property
    def patch_number(self) -> int:
        """
        The number of patches covering the zone.

        """
        return len(self._patch_extents) - 1

    @property
    def patch_extents(self) -> tuple:
        """
        The angular extents of the patches.

        """
        return self._patch_extents
