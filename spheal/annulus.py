# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines class `Annulus`.

"""

import numpy as np


class Annulus:
    """
    The 2-d region between two concentric circles.

    This class represents a natural unit for the tessellation of a disk
    consisting of cells whose boundaries are straight lines and circle arcs.

    Members
    -------

    `extents`: tuple
    The radial extents of the annulus.

    `patch_number`: int
    The number of patches in the annulus.

    `patch_extents`: tuple
    The angular extents of the patches that constitute the annulus.

    Notes
    -----

    - Each patch has exactly the same shape.

    """

    def __init__(self, extents: tuple, n_patches: int):
        """
        Parameters
        ----------

        `extents` : tuple
        A 2-d tuple containing the radial extents of the annulus.

        `n_patches` : int
        The number of azimuthal patches into which to divide the annulus.

        """
        self._extents = extents
        self._patch_extents = tuple(2.0 * np.pi * m / n_patches
                                    for m in range(n_patches + 1))

    def __lt__(self, other) -> bool:
        return self.extents[0] < other.extents[0]

    @property
    def extents(self) -> tuple:
        """
        The radial extents of the annulus.

        """
        return self._extents

    @property
    def patch_number(self) -> int:
        """
        The number of patches covering the annulus.

        """
        return len(self._patch_extents) - 1

    @property
    def patch_extents(self) -> tuple:
        """
        The extents of every patch covering the annulus.

        """
        return self._patch_extents
