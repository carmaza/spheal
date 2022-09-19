# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Exponential:

    @staticmethod
    def number_fraction(r):
        return np.exp(-2.0 * r) * (1.0 + 2.0 * r * (1.0 + r))
