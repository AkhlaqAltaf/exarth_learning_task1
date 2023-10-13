import math

from apps.hand_measurements.controller.refrence_size import RefrenceObject, area

reference_length = 283.598
pixels_per_inch = 157.33


class SelfNormalizer:
    def __init__(self ,lmlist,distance):
        self.lmlist = lmlist
        self.distance = distance
        self.distance_inches = self.normalizer()
        self.distance_cm = None



    def normalizer(self):
        x0, y0, z0 = self.lmlist[9]
        x1, y1, z1 = self.lmlist[13]

        normal_distance =math.sqrt((y1 - y0) ** 2 + (x1 - x0) ** 2)

        _normal_distance = self.distance / normal_distance
        _original_pixels = _normal_distance * reference_length


        if area !=[]:
            cm = area[0]/ pixels_per_inch
            print("Getting area...")
        else:
            cm = _original_pixels / pixels_per_inch
        self.distance_cm = cm
        cm_per_inch = 2.54
        inches = cm / cm_per_inch
        self.distance_inch = inches

        return inches
