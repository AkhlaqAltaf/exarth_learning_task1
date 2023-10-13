from apps.hand_measurements.controller.distance_finder import DistanceFinder

lengths = []
widths = []
distance_difference = []

recommendations = None


class Sizes:
    def __init__(self, lmlist):
        self.lmlist = lmlist

    def thumb(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=2, _to=4)
        return distance.get_distance

    def index_finger(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=5, _to=8)
        return distance.get_distance

    def middle_finger(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=9, _to=12)
        return distance.get_distance

    def ring_finger(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=13, _to=16)
        return distance.get_distance

    def little_finger(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=17, _to=20)
        return distance.get_distance

    def length_hand(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=0, _to=12)
        return distance.get_distance

    def width_hand(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=5, _to=17)
        return distance.get_distance

    def distance_between_thumbend_and_index_fingerstart(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=4, _to=5)
        return distance.get_distance

    def distance_between_thumbstart_and_index_fingerstart(self):
        distance = DistanceFinder(_lm_list=self.lmlist, _from=4, _to=5)
        return distance.get_distance

    def trigger_distance(self):
        # Direct match with the trigger distance of the gun
        # Assuming the first landmark is the base of the palm
        # Assuming the 9th landmark is the position of the index finger

        distance = DistanceFinder(_lm_list=self.lmlist, _from=2, _to=6)
        return distance.get_distance

    def grip_length(self):
        # Measure the length of the grip of the hand
        # Assuming the first landmark is the base of the palm
        # Assuming the 12th landmark is the tip of the middle finger

        distance = DistanceFinder(_lm_list=self.lmlist, _from=2, _to=5)
        return distance.get_distance

    def finger_thickness(self):
        # Measure the thickness of the index finger

        # Assuming the 6th landmark is the innermost point of the index finger at the base

        # Assuming the 8th landmark is the innermost point of the index finger at the middle

        distance = DistanceFinder(_lm_list=self.lmlist, _from=5, _to=7)
        return distance.get_distance



    def get_features(self):
        features_vector = [

            self.grip_length(), self.trigger_distance(),

        ]

        return features_vector
