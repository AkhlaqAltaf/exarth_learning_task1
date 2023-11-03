import os

import cv2
import imutils
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from django.conf import settings
from imutils import contours
from imutils import perspective
from scipy.spatial.distance import euclidean

from apps.hand_measurements.controller.refrence_size import RefrenceObject, area
from apps.hand_measurements.controller.sizes import Sizes

detector = HandDetector(detectionCon=0.8, maxHands=1)
sizes = None
project_directory = settings.BASE_DIR
static_directory = os.path.join(project_directory, 'media')


class HandDetector:
    def __init__(self, image):
        self.image = image

    def is_hand(self):
        frame = self.image
        hands = detector.findHands(frame)
        hand = hands[0]

        if hand:
            return True
        else:
            return False

    def get_lmlist(self):
        frame = self.image
        hands = detector.findHands(frame)
        print("Hands....",hands)
        hand = hands[0]

        if hand:
            lmlist = hand[0]
            lmlist = lmlist.get('lmList')
#TODO: it Will modifiy on the base of referece object .....................
            # ref = RefrenceObject(frame)
            # frame = ref.refrence_object()
            self.save_photo(frame, self.get_sizes(lmlist))
            return lmlist
        else:

            return None

    def get_sizes(self, lmlist):

        sizes = Sizes(lmlist=lmlist)
        return sizes

    def get_frame(self):
        frame = self.image # Make a copy of the original image
        # Get landmarks and sizes
        lmlist = self.get_lmlist()
        if lmlist is not None:
            # ref = RefrenceObject(frame)
            # frame = ref.refrence_object()
            sizes = self.get_sizes(lmlist)
            self.save_photo(frame, sizes)

    def save_photo(self, frame, sizes):
        file_path = os.path.join(static_directory, "annotated_frame.jpg")

        if sizes is not None:
            cv2.putText(frame, f"Length: {sizes.length_hand()}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)
            cv2.putText(frame, f"Width: {sizes.width_hand()}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255),
                        2)
            cv2.putText(frame, f"Distance: {sizes.distance_between_thumbend_and_index_fingerstart()}", (10, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)
            # cv2.putText(frame, f"Area: {area}", (10, 130),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1,
            #             (255, 255, 255), 2)
            image_path = cv2.imwrite(file_path, frame)
            print("Image Path....", image_path)



    def saveAnOther(self,frame):
        print("image Saving.....")
        file_path = os.path.join(static_directory, "test.jpg")


        image_path = cv2.imwrite(file_path, frame)
        print("Image Path....", image_path)