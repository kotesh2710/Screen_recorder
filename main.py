import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import time
import imageio

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
img="1.png"
ss=imageio.imread(img)

filename = f'videos/video_{str(time.strftime("%d-%m-%Y %H-%M-%S"))}.mp4'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture=cv2.VideoWriter(filename,fourcc,20.0,(width,height))


while True:
    screen = ImageGrab.grab(bbox=(0,0,width,height))
    arr = np.array(screen)
    color_img=cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)
    capture.write(color_img)
    cv2.imshow('screen',ss)
    if cv2.waitKey(1) == ord('q'):
        break


