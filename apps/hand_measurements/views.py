import os

import cv2
import mediapipe as mp
import numpy as np
from django.conf import settings
from django.shortcuts import render

from .controller.hand_measurements import HandDetector
from .controller.machine_learning.recomendation import Recommendations

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse



class View:
    feature = []
    ppi = []

    @csrf_exempt
    def upload_photo(request):

        if request.method == 'POST':
            print("Post Request..........")

            image_file = request.FILES.get('image')

            if image_file:
                print("Image File Is Post...")

                image_array = np.frombuffer(image_file.read(), np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                hand_detector = HandDetector(image)
                lmlist = hand_detector.get_lmlist()
                if lmlist:
                    sizes = hand_detector.get_sizes(lmlist=lmlist)
                    # Here is a recomendation system you should provide data in csv file
                    # also you should provide it row number that how many row you want to recommend
                    # here also it need features of hand / sizes
                    features = sizes.get_features()
                    View.feature.clear()
                    View.feature.append(features)

                    return HttpResponse("Done...")


                else:
                    # TODO : Here we will implement a message logic for notifying user

                    print("Hand is not detected...")
                    return

            else:
                return

        print("Request Was Not a post Request....")

        return

    def camera(request):
        return render(request, 'camera.html')

    def recommendations(request):

        features = View.feature[0]
        print("Features ...", features)
        recommend = Recommendations(file_name="data.csv", data_rows=5, hand_features=features)
        recommendations = recommend.simple_content_based()

        print("Recomendations....", recommendations)

        return render(request, "recommendations.html", {"recommendations": recommendations})


    def view_ppi(request):
        ppi = View.ppi[0]
        return render(request, "view_ppi.html", {"ppi": ppi})

    @csrf_exempt
    def get_frame(request):
        print("Enter ...............")

        if request.method == 'POST':
            print("Post Request..........")

            image_file = request.FILES.get('image')

            if image_file:
                print("Image File Is Post...")

                image_array = np.frombuffer(image_file.read(), np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                # This part of code will detect hand
                # if hand is detecting than it will process on machine learning
                print(image)
                hand_detector = HandDetector(image)

                if hand_detector.is_hand():
                    print("Hand is detecting...")
                    # this method return lmlist
                    frame_url = hand_detector.get_frame()
                    print("Frame URL..." ,frame_url)

                    print("Frame Type..." ,type(frame_url))

                    return JsonResponse({'frame': frame_url})


                else:
                    # TODO : Here we will implement a message logic for notifying user

                    print("Hand is not detected...")
                    return

            else:
                return

        print("Request Was Not a post Request....")

        return


    def croping(request):

        return render(request,"croping/index.html" )
