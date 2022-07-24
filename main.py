import cv2
import mediapipe as mp
import pyautogui
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)

    hand = detector.findHands(img, draw=False)
    fing = cv2.imread("0finger.jpg")
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread("1finger.png")
                pyautogui.press('volumeup')

            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread("2fingers.png")
                pyautogui.press('volumedown')

            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread("3fingers.png")
                pyautogui.press('prevtrack')
                pyautogui.sleep(0.5)
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread("4fingers.jpg")
                pyautogui.press('nexttrack')
                pyautogui.sleep(0.5)
            if fingerup == [1, 1, 1, 1, 1]:
               fing =cv2.imread('5.jpg')
               print("blahblah")
               pyautogui.press('playpause')
               pyautogui.sleep(1)

    img[50:330, 20:240] = fing
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('here')
        break

