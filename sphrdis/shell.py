# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


def particle_number(numbers, profile, N, r):
    """
    Calculate the number of particles in each given shell.

    Arguments
    ---------

    `numbers` : ndarray(uint32)
    The array where to store the number of particles in each shell.

    `profile` : obj
    The spherically symmetric profile used to calculate the fraction of
    particles at a given radius. Must have a `number_fraction(r)` member.

    `N` : int
    The total number of particles across all shells.

    `r` : ndarray
    The radial extensions of every shell, i.e. the nth shell extends between
    `r = [r[n], r[n-1]]`.

    """
    if not numbers.dtype == np.uint32:
        msg = "Type of numbers should be np.uint32. Got " + str(numbers.dtype)
        raise TypeError(msg)

    f = profile.number_fraction(r)
    numbers[:] = N * np.array(
        [f[j - 1] - f[j] for j in range(1,
                                        len(numbers) + 1)])
