from custom_socket import CustomSocket
import cv2
import numpy as np

HOST = "127.0.0.1"
PORT = 9005

socket = CustomSocket(HOST,PORT)
socket.startServer()

listen = True

while True :
	conn, addr = socket.s.accept()
	print("Connected :", addr, listen)

	if listen :
		data = b''
		while True :
			res = conn.recv(1024)
			if not res :
				break
			data += res
		img = np.frombuffer(data,dtype=np.uint8).reshape((720,1080,3))
		print(img.shape)
	else :
		conn.sendall(str(img.mean()).encode('utf-8'))
	listen = not listen
	conn.close()
