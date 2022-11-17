# Distributed under the MIT License.
# See LICENSE for details.

import abc


class Profile(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def r90(self):
        pass

    @abc.abstractmethod
    def particle_number(r):
        pass
