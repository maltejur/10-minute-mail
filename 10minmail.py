#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# depends on websocket-client and pyperclip
import websocket
import pyperclip
import sys
import os
from json import loads
from datetime import datetime

class mailbox(object):
	"""10 minute mailbox"""
	def __init__(self):
		super(mailbox, self).__init__()
		self.ws = websocket.WebSocket()
		self.ws.connect("wss://dropmail.me/websocket")
		self.next = self.ws.recv
		self.close = self.ws.close
		self.email = self.next()[1:].split(":")[0]
		self.next()

def main(box):
	pyperclip.copy(box.email)
	print (box.email+" was copied to clipboard")
	while True:
		result =  box.next()
		try:
			print("Recieved following at {0}".format( datetime.now()))
			for k in loads(result[1:]).items():
				print("\t%s: %s" % k)
		except:
			print("Recieved:{1} {0}\n".format(result, datetime.now()))

if __name__ == '__main__':
	try:
		box = mailbox()
		main(box)
	except KeyboardInterrupt:
		box.close()
		sys.exit(0)