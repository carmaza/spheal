# Distributed under the MIT License.
# See LICENSE for details.

import matplotlib.pyplot as plt
import numpy as np

from spheal.zone import Zone


class Hemisphere:
    """
    Equal-area hemisphere tessellation based on Beckers & Beckers (2012).

    This tesselation accommodates an exact given number of patches on the
    hemisphere. The hemisphere is divided into zones of variable number of
    patches (i.e. no congruency), and every patch throughout the hemisphere
    has exactly the same surface area. 

    Parameters
    ----------

    `radius`: float
    The radius of the hemisphere.

    `n_patches`: int
    The total number of patches to use in the tessellation.

    `aspect`: float
    The constant aspect ratio that the algorithm tries to give to each patch.

    `draw`: bool (default: False)
    Whether to draw the resulting tessellation to a PDF.

    Members
    -------
    
    `zones`: list
    The zones that constitute the hemisphere.

    `radius` : float
    The radius of the hemisphere.

    `patch_number`: int
    The total number of patches in the hemisphere.

    Notes
    -----

    - Every patch's aspect ratio will only be _approximately_ equal to the given
      aspect ratio. This is because the aspect ratio is computed given the
      number of patches at two adjacent zones, and float rounding happens
      when computing the number of patches in each zone.

    - For a given number of patches, aspect ratios too low or too high might
      fail to converge to a solution. For instance, for 1000 patches, aspect
      ratios > 50 and < 0.15 are prone to give inaccurate results.

    """

    def __init__(self,
                 radius: float,
                 n_patches: int,
                 patch_aspect: float,
                 draw=False):
        self._radius = radius
        self._patch_aspect = patch_aspect

        l = 0
        theta_lm1 = 0.5 * np.pi
        r_lm1 = self._r(theta_lm1)
        k_lm1 = n_patches

        # Maximum integer l for which theta_l > 0.
        lmax = np.floor(
            (radius * theta_lm1 / r_lm1) *
            np.sqrt(n_patches * patch_aspect / np.pi)).astype(dtype=np.int64)

        self._zones = []
        while l < lmax:
            l += 1
            theta_l = self._theta_l(theta_lm1, r_lm1, k_lm1)
            r_l = self._r(theta_l)
            k_l = self._k_l(k_lm1, r_lm1, r_l)

            if l == lmax:
                r_inn = r_lm1 / np.sqrt(k_lm1)
                theta_inn = 2. * np.arcsin(0.5 * r_inn / radius)
                self._zones.append(Zone((theta_inn, theta_lm1), k_lm1 - 1))
                self._zones.append(Zone((0., theta_inn), 1))

            else:
                self._zones.append(Zone((theta_l, theta_lm1), k_lm1 - k_l))
                theta_lm1, r_lm1, k_lm1 = theta_l, r_l, k_l

        if draw:
            self.draw_lambert_proj()

    @property
    def zones(self):
        return self._zones

    @property
    def radius(self):
        return self._radius

    @property
    def patch_number(self):
        return sum(zone.patch_number for zone in self._zones)

    # Eq. (1)
    def _k_l(self, k_lm1, r_lm1, r_l):
        return np.rint(k_lm1 * (r_l / r_lm1)**2.0).astype(dtype=np.int64)

    # Eq. (16)
    def _r(self, theta):
        return 2.0 * self._radius * np.sin(0.5 * theta)

    # Eq. (20)
    def _theta_l(self, theta_lm1, r_lm1, k_lm1):
        return theta_lm1 - r_lm1 * np.sqrt(
            np.pi / self._patch_aspect / k_lm1) / self._radius

    def draw_lambert_proj(self, name="Projection"):
        """
        Draw Lambert projection of the tesselation to PDF.
        """
        dense_phi = np.linspace(0., 2. * np.pi, 100)
        dense_cos, dense_sin = np.cos(dense_phi), np.sin(dense_phi)

        fig, ax = plt.subplots()
        for zone in self._zones:
            ri, ro = self._r(zone.extents[0]), self._r(zone.extents[1])
            phi = zone.patch_extents
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
        plt.savefig(f"{name}.pdf", bbox_inches="tight")
        plt.close(fig)
