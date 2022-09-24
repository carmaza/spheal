# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


def cartesian_from_spherical(coords, r, theta, phi):
    coords[:, 0] = r[:] * np.sin(theta[:]) * np.cos(phi[:])
    coords[:, 1] = r[:] * np.sin(theta[:]) * np.sin(phi[:])
    coords[:, 2] = r[:] * np.cos(theta[:])


def rotate_about(v, k, a):
    v[:] = v * np.cos(a) + np.cross(k, v) * np.sin(a) + k * np.dot(
        k, v) * (1.0 - np.cos(a))
