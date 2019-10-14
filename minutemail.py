#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# depends on websocket-client and pyperclip
import websocket
import pyperclip
import sys
import os
import requests
import re
from json import loads
from datetime import datetime

class mailbox(object):
	"""10 minute mailbox"""
	def __init__(self):
		super(mailbox, self).__init__()
		self.ws = websocket.WebSocket()
		self.ws.connect("wss://dropmail.me/websocket")
		self.close = self.ws.close
		self.email = self.ws.recv()[1:].split(":")[0]
		self.ws.recv()
	def next(self,html=True):
		mail = loads(self.ws.recv()[1:])
		request = requests.get("https://dropmail.me/download/mail/"+self.email+"/"+mail["ref"])
		if html: 
			try:
				mail["html"] = re.search(r"Content-Type: text\/html;.*?\r\n.*?\r\n\r\n((.|\n)*)\r\n\r\n--------------",request.text).group(1)
			except AttributeError:
				pass
		return mail

def main(box):
	pyperclip.copy(box.email)
	print (box.email+" was copied to clipboard")
	while True:
		result =  box.next()
		print("\nRecieved following at {0}".format( datetime.now()))
		try:
			for k in result:
				print("{0}: {1}".format(k, result[k]))
		except:
			print(result)

if __name__ == '__main__':
	try:
		box = mailbox()
		main(box)
	except KeyboardInterrupt:
		box.close()
		sys.exit(0)