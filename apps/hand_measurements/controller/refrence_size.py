import cv2
import numpy as np

area = []


class RefrenceObject:

    def __init__(self, image):
        self.image = image

    def is_sqaure(self, approx):

        distances = [np.linalg.norm(approx[i] - approx[(i + 1) % len(approx)]) for i in range(len(approx))]
        print("Distances between consecutive points:", distances)

        # Calculate differences between consecutive distances
        differences = [distances[i] - distances[(i + 1) % len(distances)] for i in range(len(distances))]
        print("Differences between consecutive distances:", differences)

        # Check if the differences are not more than 100
        if all(abs(diff) < 100 for diff in differences):
            print("Potential Square!")

            return True

        else:
            print("Not Area is Founded....")
            return False

    def getContours(self, img_dilate, img_contour):
        contours, hierachy = cv2.findContours(img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for cnt in contours:
            are = cv2.contourArea(cnt)
            if are > 1000:
                print(cnt)

                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                print(approx)
                print("Length : ", len(approx))

                if len(approx)==4:
                    area.clear()
                    area.append(are)
                    cv2.drawContours(img_contour, cnt, -1, (255, 0, 255), 7)
                    print("Area ,..: ",area)
                    return are
                else:
                    print("Approximate Refrence Object should have same ends")
                    return None
                print(_sqaure)

    def refrence_object(self):
        print("Enter in Reference Object......")
        img = self.image
        img_contour = img.copy()
        img_blur = cv2.GaussianBlur(img, (7, 7), 1)
        img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
        threshold1 = 20  # cv2.getTrackbarPos("Threshold1" , "Parameters")
        threshold2 = 60  # cv2.getTrackbarPos("Threshold2" , "Parameters")
        img_canny = cv2.Canny(img_gray, threshold1, threshold2)

        # Image Dilation for removing noise
        kernal = np.ones((5, 5))
        img_dil = cv2.dilate(img_canny, kernal, iterations=1)

        self.getContours(img_dil, img_contour)

        return img_contour
