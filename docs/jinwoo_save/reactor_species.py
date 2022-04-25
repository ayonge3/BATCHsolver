
# Copyright 2021, Battelle Energy Alliance, LLC All Rights Reserved


import pandas as pd
import numpy as np
import math as mp
from define_gas import define_gas
from define_adspecies import define_adspecies

class reactor_species():

	"""
	
	This class acts as a container for all of the assumed initial conditions of an experiment.
	
	Args:
		
		gasses (dict of ): The  

	"""

	def __init__(self, inert_diffusion = 16, catalyst_diffusion = 16, reference_temperature = 385.6, reference_mass = 40, temperature = 385.6):
		self.gasses = {}
		self.inert_gasses = {}
		self.adspecies = {}
		self.reference_temperature = reference_temperature
		self.temperature = temperature
		self.reference_pulse_size = 1
		
	def add_gas(self,name='', define_gas_data = define_gas):
		
		if name not in self.gasses:
			self.gasses[name] = define_gas_data
		else:
			print('Gas already defined in dictionary.')

	def add_inert_gas(self,name='', define_gas_data = define_gas):
		
		if name not in self.gasses:
			self.inert_gasses[name] = define_gas_data
		else:
			print('Gas already defined in dictionary.')

	def add_adspecies(self,name='', define_adspecies_data = define_adspecies):
		
		if name not in self.adspecies:
			self.adspecies[name] = define_adspecies_data
		else:
			print('Gas already defined in dictionary.')		
