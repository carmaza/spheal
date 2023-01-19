# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines the following functions related to vectors in Euclidean space:

- `cartesian_from_spherical(coords, r, theta, phi)`
  Computes Cartesian coordinates from spherical coordinates.

- spherical_from_cartesian(theta, phi, x, y, z, r=None)`
  Computes spherical coordinates from Cartesian coordinates.

- `rotate_about(v, k a)`
  Rotates a vector using Rodrigues's axis-angle formula.

"""

import numpy as np


def cartesian_from_spherical(coords, r, theta, phi):
    """
    Compute Cartesian coordinates of the given spherical coordinates.

    Parameters
    ---------

    `coords` : ndarray(N, 3)
    The `x, y, z` Cartesian coordinates as N rows.

    `r, theta, phi` : ndarray(N)
    The angular coordinates of each of the N points.

    """
    coords[:, 0] = r[:] * np.sin(theta[:]) * np.cos(phi[:])
    coords[:, 1] = r[:] * np.sin(theta[:]) * np.sin(phi[:])
    coords[:, 2] = r[:] * np.cos(theta[:])


def spherical_from_cartesian(theta, phi, x, y, z, r=None):
    """
    Compute spherical angles of the given Cartesian coordinates.

    Parameters
    ---------

    `theta, phi` : ndarray, ndarray
    The spherical angles.

    `x, y, z` : ndarray, ndarray, ndarray
    The Cartesian coordinates.

    `r` : ndarray (optional, default: None)
    The radial coordinate, precomputed as r = sqrt(x*x + y*y + z*z). If not
    given, this function will compute it internally. Note that this argument
    is a convenience, for r is usually expected to be needed in other
    calculations outside of this function.

    """
    if r is None:
        r = np.sqrt(x * x + y * y + z * z)

    theta[:] = np.arccos(z[:] / r[:])
    phi[:] = np.arctan2(y[:], x[:])


def rotate_about(v, k, a):
    """
    Rotate a given vector according to Rodrigues's axis-angle formula.

    Parameters
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
