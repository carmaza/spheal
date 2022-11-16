# Distributed under the MIT License.
# See LICENSE for details.

import matplotlib.pyplot as plt
import numpy as np

from sphrdis.annulus import Annulus


class Disk:
    """
    Equal-area disk tessellation based on Beckers & Beckers (2012).

    This tesselation accommodates an exact given number of patches on the disk.
    The disk is divided into annuli of variable number of patches (i.e. no
    congruency), and every patch throughout the disk has exactly the same
    surface area. 

    Parameters
    ----------

    `radius`: float
    The radius of the disk.

    `n_patches`: int
    The total number of patches to use in the tessellation.

    `aspect`: float
    The constant aspect ratio that the algorithm tries to give to each patch.

    `draw`: bool (default: False)
    Whether to draw the resulting tessellation to a PDF.

    Members
    -------
    
    `annuli`: list
    The annuli that constitute the disk.

    `radius` : float
    The radius of the disk.

    `patch_number`: int
    The total number of patches in the disk.

    Notes
    -----

    - Every patch's aspect ratio will only be _approximately_ equal to the given
      aspect ratio. This is because the aspect ratio is computed given the
      number of patches at two adjacent annuli, and float rounding happens
      when computing the number of patches in each annulus.

    - For a given number of patches, aspect ratios too low or too high might
      fail to converge to a solution. For instance, for 1000 patches, aspect
      ratios > 50 and < 0.15 are prone to give innacurate results.

    """

    def __init__(self,
                 radius: float,
                 n_patches: int,
                 patch_aspect: float,
                 draw=False,
                 filename="Disk",
                 fmt="pdf"):
        self._radius = radius
        self._patch_aspect = patch_aspect

        # Maximum integer l for which k_l > 0.
        lmax = np.floor(np.sqrt(n_patches * patch_aspect /
                                np.pi)).astype(dtype=np.int64)

        l = 0
        k_lm1, r_lm1 = n_patches, radius

        self._annuli = []
        while (l < lmax):
            l += 1
            k_l = self._k_l(k_lm1)
            r_l = self._r_l(r_lm1, k_lm1, k_l)

            if l == lmax:
                # Force innermost patch to be a concentric circle.
                r_inn = r_lm1 / np.sqrt(k_lm1)
                self._annuli.append(Annulus((r_inn, r_lm1), k_lm1 - 1))
                self._annuli.append(Annulus((0., r_inn), 1))
            else:
                self._annuli.append(Annulus((r_l, r_lm1), k_lm1 - k_l))
                k_lm1, r_lm1 = k_l, r_l

        if draw:
            self.draw(filename, fmt)

    @property
    def annuli(self):
        return self._annuli

    @property
    def radius(self):
        return self._radius

    @property
    def patch_number(self):
        return sum(annulus.patch_number for annulus in self._annuli)

    # Eq. (1)
    def _r_l(self, r_lm1, k_lm1, k_l):
        return r_lm1 * np.sqrt(k_l / k_lm1)

    # Eq. (3)
    def _a_l(self, k_lm1, k_l):
        return np.pi / (np.sqrt(k_l) - np.sqrt(k_lm1))**2.0

    # Eq. (13)
    def _k_l(self, k_lm1):
        return np.rint(
            (np.sqrt(k_lm1) -
             np.sqrt(np.pi / self._patch_aspect))**2.0).astype(dtype=np.int64)

    def draw(self, name="Disk", fmt="pdf"):
        """
        Draw tesselation to file.
        """
        dense_phi = np.linspace(0., 2. * np.pi, 100)
        dense_cos, dense_sin = np.cos(dense_phi), np.sin(dense_phi)

        fig, ax = plt.subplots()
        for annulus in self._annuli:
            ri, ro = annulus.extents
            phi = annulus.patch_extents
            cos_phi, sin_phi = np.cos(phi), np.sin(phi)
            if len(phi) > 2:
                ax.plot(np.array([ri * cos_phi, ro * cos_phi]),
                        np.array([ri * sin_phi, ro * sin_phi]),
                        color="purple",
                        linewidth=0.3)
            ax.plot(ro * dense_cos,
                    ro * dense_sin,
                    color="purple",
                    linewidth=0.3)

        ax.set_aspect(1.0)
        plt.savefig("{}.{}".format(name, fmt), bbox_inches="tight", dpi=300)
        plt.close()
