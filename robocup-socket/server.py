from custom_socket import CustomSocket
import cv2
import numpy as np

NAME = "TEST"
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



# import socket
# from cStringIO import StringIO
# import numpy as np
# import cv2
# import time

# s = socket.socket()
# s.bind(("127.0.0.1",9002))
# s.listen(5)
# listen = True
# while True :
# 	conn, addr = s.accept()	
# 	print "Connected by :", addr, listen

# 	if listen :
# 		data = ""
# 		while True :
# 			res = conn.recv(1024)
# 			if not res :
# 				break
# 			data += res

# 		image = np.frombuffer(data,dtype=np.uint8).reshape(720,1080,3)
# 		print image.shape
# 		listen = False

# 	else :
# 		time.sleep(10)
# 		conn.sendall("person")
# 		listen = True

# 	conn.close()
