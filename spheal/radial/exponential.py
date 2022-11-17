# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np

from spheal.radial.profile import Profile


class Exponential(Profile):

    def __init__(self):
        self._r90 = 2.661160168917105

    @property
    def r90(self):
        return self._r90

    @staticmethod
    def particle_number(r):
        return 1.0 - np.exp(-2.0 * r) * (1.0 + 2.0 * r * (1.0 + r))
