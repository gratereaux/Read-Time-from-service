#!/usr/bin python

import json
import urllib2
from time import gmtime, strftime


""" Abriendo json2 de worldtime """

def obtenerhora():

	url  = "http://ventas.orange.com.do/test2/time.php"
	req = urllib2.Request(url)
	opener = urllib2.build_opener()
	urlopen = opener.open(req)
	time = json.loads(urlopen.read())

	hora = time['tm_hour']
	minuto = time['tm_min']
	segundo = time['tm_sec']

	if (hora > 12):
		hora = hora - 12
		que = "PM"
	else:
		que = "AM"

	if (minuto < 10):
		minuto = "0"+ str(minuto)

	return str(hora) + ":" + str(minuto) + ":" + str(segundo)+ " " + que

print " hora json : " + obtenerhora()

horaa = int(strftime("%I", gmtime()))

print " hora servidor local : " + str(horaa-4) + strftime(":%M:%S %p", gmtime())