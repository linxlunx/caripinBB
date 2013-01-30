#!/usr/bin/env python

import urllib2
import json
import re

ambil = urllib2.urlopen("http://search.twitter.com/search.json?q=pin%20BB&rpp=100&include_entities=true&result_type=mixed")
hasil = json.loads(ambil.read())
twit = [i['text'] for i in hasil['results']]
bersih = re.compile(r"[^a-zA-Z0-9]+")
hasilbersih = bersih.sub(" "," ".join(twit))
bebe = [i for i in hasilbersih.split() if re.search("^2|^3",i) and len(i) == 8]
for i in bebe:
	print i
