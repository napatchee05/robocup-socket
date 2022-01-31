import socket
import struct

class CustomSocket :

	def __init__(self,host,port) :
		self.host = host
		self.port = port
		self.sock = socket.socket()
		self.isServer = False

	def startServer(self) :
		try :
			self.sock.bind((self.host,self.port))
			self.sock.listen(5)
			self.isServer = True
			print("[SOCKET SERVER START AT PORT "+str(self.port)+"]")
		except Exception as e :
			print("Error :",e)
			return False
		return True

	def clientConnect(self) :
		try :
			self.sock.connect((self.host,self.port))
		except Exception as e :
			print("Error :",e)
			return False
		return True

	def sendMsg(self,sock,msg) :
		msg = struct.pack('>I', len(msg)) + msg.encode('utf-8')
		sock.sendall(msg)

	def recvall(self,sock,n) :
		data = bytearray()
		while len(data) < n :
			packet = sock.recv(n - len(data))
			if not packet :
				return None
			data.extend(packet)
		return data

	def recvMsg(self,sock) :
		rawMsgLen = self.recvall(sock, 4)
		if not rawMsgLen :
			return None
		msgLen = struct.unpack('>I', rawMsgLen)[0]
		return self.recvall(sock, msgLen).decode('utf-8')


def main() :

	server = CustomSocket(socket.gethostname(),10000)
	server.startServer()

	while True :
		conn, addr = server.sock.accept()
		print("Connected from",addr)
		data = server.recvMsg(conn)
		print(data)
		server.sendMsg(conn,data[::-1])

if __name__ == '__main__' :
	main()	


