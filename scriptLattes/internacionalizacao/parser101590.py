#!/usr/bin/python
# caso 2 http://www.scielo.br/ procura entre o 7mo y 10mo <p>
import  unicodedata
#The module is called html.parser in Python 3
from html.parser import HTMLParser


class parser101590(HTMLParser):
    	def __init__(self):
	    HTMLParser.__init__(self)
	    self.recording = 0 
	    self.data = []
	    self.count=0
	def handle_starttag(self, tag, attrs):
	    if tag=='p':
		self.count=self.count+1
		self.recording = 1
	def handle_endtag(self, tag):
	    if tag == 'p':
		if self.recording == 1:
	      		self.recording -=1
	def handle_data(self, data):
	    if self.recording and self.count > 4 and self.count < 11:			
			data = ''.join((c for c in unicodedata.normalize('NFD',data) if unicodedata.category(c) != 'Mn'))
			self.data.append(data)
	
