import socket

def initSocket(host,port) :
	s = socket.socket()
	s.connect((host,port))
	return s

class CustomSocket :

	def __init__(self,host,port) :
		self.host = host
		self.port = port
		self.s = socket.socket()

	def startServer(self) :
		try :
			self.s.bind((self.host,self.port))
			self.s.listen(5)
			print("[SOCKET SERVER START AT PORT "+str(self.port)+"]")
		except Exception as e :
			print("Error :",e)
			return False
		return True

	def getMean(self,img) :
		cs = socket.socket()
		cs.connect((self.host,self.port))
		cs.sendall(img.tobytes())
		cs.close()
		cs = socket.socket()
		cs.connect((self.host,self.port))
		return cs.recv(1024).decode('utf-8')
