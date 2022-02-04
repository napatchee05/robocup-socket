import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket

img = cv2.imread("test3.jpg")

print(img.shape)

host = socket.gethostname()
port = 10000

c = CustomSocket(host,port)
c.clientConnect()

cap = cv2.VideoCapture(1)

while True :

	ret, frame = cap.read()

	if not ret :
		break

	try :
		res = c.req(frame)
		print(res)
	except Exception as e :
		print(e)

cv2.destroyAllWindows() 














