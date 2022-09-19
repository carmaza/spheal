# Distributed under the MIT License.
# See LICENSE for details.

import numpy as np


class Exponential:

    @staticmethod
    def partial_number_density(r):
        return np.exp(-2.0 * r) * (1.0 + 2.0 * r * (1.0 + r))
