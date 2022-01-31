import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket

img = cv2.imread("test3.jpg")
print img.shape

host = "127.0.0.1"
port = 9005

meanSocket = CustomSocket(host,port)
mean = meanSocket.getMean(img)
print(mean)














