#!/usr/bin/env python3 
import sys, getopt
import socket
class send_er : 
	con_statue = True 

	def send(self,s_data,Connection): 			   
		try : 
			Connection.sendall(s_data)
			data = Connection.recv(1024)
			print("sendig data ")
		except : 
			self.con_statue = False 
			print("Some errore in connection !!")


opts, args = getopt.getopt(sys.argv[1:],"sp")
op = opts[0][0]


try : 
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as con:
		sender = send_er() 
		con.connect(("localhost",1111))
		if op == '-s' : 

			sender.send(b'next',con)
		elif op == '-p' : 
			sender.send(b'prev',con)

		con.close() 

except : 
	print("Connection refuse !!")
