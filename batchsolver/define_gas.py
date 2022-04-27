
# Copyright 2021, Battelle Energy Alliance, LLC All Rights Reserved

import pandas as pd
import numpy as np
import math as mp
#from structures import reactor_species

class define_gas():
	def __init__(self, mass = 0):
		self.concentration = 0
		self.noise = 0.0
		self.sigma = 0.0