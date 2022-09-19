# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


def cartesian_from_spherical(coords, r, theta, phi):
    coords[:, 0] = r[:] * np.sin(theta[:]) * np.cos(phi[:])
    coords[:, 1] = r[:] * np.sin(theta[:]) * np.sin(phi[:])
    coords[:, 2] = r[:] * np.cos(theta[:])
