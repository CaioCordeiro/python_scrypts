import serial
import time
import cv2
import facebook
from PIL import Image

graph = facebook.GraphAPI(access_token="EAADXkI2RPRABABOFQ4Lm0b595kvZADjw9hhGL7cCWo08uaIDVXGPaH222xPVnF2amBxANpf98JN0f0IylhAblmjIjLalZBvNZBrClVoYOqTRFxZCeXSli9mWVNkc8yVc1ci7iIhw2qzdaD1QuUVJoZCXISTXVfYUCU7h2GHjs2JBYd87HWU8CYZCK7fSAAdB1ZBJ6KnuxYkVM5GWWeXQVVO", version="2.7")



cap = cv2.VideoCapture(0)

counter = 0

def show_webcam(mirror=False): 
    cv2.namedWindow('Som na Rural',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()                 
        if mirror:
            frame = cv2.flip(frame, 1)
            cv2.imshow('Som na Rural', frame)                               
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
while True:
    show_webcam(mirror=True)
