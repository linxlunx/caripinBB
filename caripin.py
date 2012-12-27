#!/usr/bin/env python

import urllib2
import json
import re
from threading import Thread

replace = {",":" ", ".":" ", ":":" ", "!":" ", "?":" "}

class ambilpin(Thread):
	def __init__(self, kalimat):
		Thread.__init__(self)
		self.kalimat = kalimat
		self.pinBB = ""
	def run(self):
		kalimatnya = reduce(lambda a, kv: a.replace(*kv), replace.iteritems(), self.kalimat)
		for j in kalimatnya.split():
			if re.search("^2|^3",j) and len(j) == 8:
				self.pinBB = j

bebe = []

ambil = urllib2.urlopen("http://search.twitter.com/search.json?q=pin%20BB&rpp=100&include_entities=true&result_type=mixed")
hasil = json.loads(ambil.read())
for i in hasil['results']:
	kalimat = i['text']
	proses = ambilpin(kalimat)
	bebe.append(proses)
	proses.start()

for i in bebe:
	i.join()
	if len(i.pinBB) > 0:
		print i.pinBB
