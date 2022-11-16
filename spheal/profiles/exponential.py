# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Exponential:

    def __init__(self):
        self._r90 = 2.661

    @property
    def r90(self):
        return self._r90

    @staticmethod
    def number_fraction(r):
        return np.exp(-2.0 * r) * (1.0 + 2.0 * r * (1.0 + r))