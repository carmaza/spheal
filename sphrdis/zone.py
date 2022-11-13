# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Zone:
    """
    The surface of a spherical segment (excluding the bases).

    This class represents a natural unit for the tessellation of a hemisphere
    consisting of cells whose boundaries are parallel and meridian arcs.

    Parameters
    ----------

    `extents`: tuple
    a 2-d tuple containing the zenithal extents of the zone.

    `n_patches`: int
    The number of azimuthal patches into which to divide the zone.

    Members
    -------

    `extents`: tuple
    The zenithal extents of the zone.

    `patch_extents`: tuple
    The azimuthal extents of the patches that constitute the zone.

    Notes
    -----

    - Each patch has exactly the same shape.
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
