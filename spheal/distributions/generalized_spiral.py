# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines class `GeneralizedSpiral`.

"""

import numpy as np


class GeneralizedSpiral:
    """
    The parameterized spiraling scheme introduced by Saff & Kuijlaars (1997).

    Attributes
    ----------

    `N` : float
    The number of particles in the distribution.

    `theta` : ndarray
    The zenithal coordinate of every particle.

    `phi` : ndarray
    The azimuthal coordinate of every particle.

    """

    def __init__(self, N):
        self._N = N
        self._theta = np.empty(N)
        self._phi = np.empty(N)

        self._set_angles(self._theta, self._phi)

    @property
    def N(self):
        """
        The number of particles in the distribution.

        """
        return self._N

    @property
    def theta(self):
        """
        The zenithal cordinate of every particle.

        """
        return self._theta

    @property
    def phi(self):
        """
        The azimuthal coordinate of every particle.

        """
        return self._phi

    def _h(self, k):
        N = self._N
        if k < 1 or k > N:
            ValueError("Value of k should be in range [1, N].")
        return -1.0 + 2.0 * (k - 1.0) / (N - 1.0)

    def _phase(self, hk):
        return 3.6 / np.sqrt(self._N) / np.sqrt(1.0 - hk**2)

    def _set_angles(self, theta, phi):
        N = self._N

        hk = np.array([self._h(k) for k in range(1, N + 1)])
        theta[:] = np.arccos(hk)

        for k in range(N):
            phi[k] = 0.0 if k == 0 or k == N - 1 else phi[k - 1] + self._phase(
                hk[k])
