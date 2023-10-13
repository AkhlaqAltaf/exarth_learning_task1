import math

from apps.hand_measurements.controller.self_normalizer import SelfNormalizer


class DistanceFinder:
    def __init__(self, _lm_list, _from, _to):
        self._lm_list = _lm_list
        self._from = _from
        self._to = _to
        self.get_distance = self.distance()

    def distance(self):

        distance_from = self._lm_list[self._from]
        distance_to = self._lm_list[self._to]
        x0, y0,z0 = distance_from
        x1, y1,z1 = distance_to
        print(x0 , y0 , x1 , y1)

        distance = math.sqrt((y1 - y0) ** 2 + (x1 - x0) ** 2)
        distance_normalizer = SelfNormalizer(lmlist=self._lm_list, distance=distance)

        return distance_normalizer.distance_inch

