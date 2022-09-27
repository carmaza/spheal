# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


def cartesian_from_spherical(coords, r, theta, phi):
    """
    Compute Cartesian coordinates of the given spherical coordinates.

    Arguments
    ---------

    `coords` : ndarray(N, 3)
    The `x, y, z` Cartesian coordinates as N rows.

    `r, theta, phi` : ndarray(N)
    The angular coordinates of each of the N points.

    """
    coords[:, 0] = r[:] * np.sin(theta[:]) * np.cos(phi[:])
    coords[:, 1] = r[:] * np.sin(theta[:]) * np.sin(phi[:])
    coords[:, 2] = r[:] * np.cos(theta[:])


def rotate_about(v, k, a):
    """
    Rotate a given vector according to Rodrigues' axis-angle formula.

    Arguments
    ---------

    `v` : ndarray(3)
    The vector to rotate.

    `k`: ndarray(3)
    The axis of rotation. Must be a unit vector.

    `a` : float
    The angle of rotation in radians.

    """
    v[:] = v * np.cos(a) + np.cross(k, v) * np.sin(a) + k * np.dot(
        k, v) * (1.0 - np.cos(a))
