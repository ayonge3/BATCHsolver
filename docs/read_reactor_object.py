from .reactor import reactor
#from structures import reactor
import jsonpickle
import json
import sys

def read_reactor_object(file_name):

	loaded_reactor = reactor()

	with open(file_name) as f:
		data = json.loads(f.read())
	f.close()

	sameObject = jsonpickle.decode(data)
	sameObject2 = sameObject["1"]

	loaded_reactor.temperature = sameObject2.temperature	

	return loaded_reactor