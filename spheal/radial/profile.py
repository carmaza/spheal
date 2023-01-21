# Distributed under the MIT License.
# See LICENSE for details.
"""
Defines `Profile`, the base class for radial profiles.

"""

import abc


class Profile(metaclass=abc.ABCMeta):
    """
    Base class for radial profiles. Each derived class should define the
    following members:

    Attributes
    ----------

    `r90` : float
    The radius containing 90% of the total number of particles.

    Functions
    ---------

    `particle_number(r)`
    The number of particles contained at the given radius r.

    """

    @property
    @abc.abstractmethod
    def r90(self):
        """
        Return the radius enclosing 90% of the particles.

        """

    @staticmethod
    @abc.abstractmethod
    def particle_number(r):
        """
        Compute the number of particles enclosed in a radius r.

        """
