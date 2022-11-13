# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Annulus:
    """
    The 2-d region between two concentric circles.

    This class represents a natural unit for the tessellation of a disk
    consisting of cells whose boundaries are straight lines and circle arcs.

    Parameters
    ----------

    `extents`: tuple
    A 2-d tuple containing the radial extents of the annulus.

    `n_patches`: int
    The number of azimuthal patches into which to divide the annulus.

    Members
    -------

    `extents`: tuple
    The radial extents of the annulus.

    `patch_extents`: tuple
    The angualr extents of the patches that constitute the annulus.

    Notes
    -----

    - Each patch has exactlu the same shape.
    """

    def __init__(self, extents: tuple, n_patches: int):
        self._extents = extents
        self._patch_extents = tuple(2.0 * np.pi * m / n_patches
                                    for m in range(n_patches + 1))

    @property
    def extents(self) -> tuple:
        return self._extents

    @property
    def patch_extents(self) -> tuple:
        return self._patch_extents
