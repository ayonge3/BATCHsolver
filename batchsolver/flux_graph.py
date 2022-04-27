#from structures import *
from .define_adspecies import define_adspecies
from .define_gas import define_gas
from .experimental_data import experimental_data
from .mechanism import mechanism
from .reactor import reactor
from .reactor_species import reactor_species
#from read_old_input import read_old_input
from .TAPobject import TAPobject

#from file_io import *
from .new_experiments import new_experiments
from .read_experimental_data_object import read_experimental_data_object
from .read_mechanism_object import read_mechanism_object
from .read_reactor_object import read_reactor_object
from .read_reactor_species_object import read_reactor_species_object 
from .read_TAPobject import read_TAPobject 
from .read_transient_sensitivity import read_transient_sensitivity 
from .save_object import save_object
#from vary_input_file import vary_input_file

#from mechanism_construction import *
#from construct_batch_equation import make_batch_equation
from .construct_f_equation import construct_f_equation
from .construct_f_equation_multiple_experiments import construct_f_equation_multiple_experiments
from .construct_rate_equations import rateEqs
from .elementary_process import elementary_process
from .elementary_process_details import elementary_process_details
from .mechanism_constructor import mechanism_constructor
from .mechanism_reactants import mechanism_reactants

#from reference_parameters import *
from .reference_parameters import load_standard_parameters

#from simulation_notes import *
from .timing_details import *
from .error_details import *

#from inverse_problem import *
from .define_fitting_species import curveFitting
#from point_objective import point_objective
from .std_objective import stdEstablishment
from .total_objective import curveFitting
import matplotlib.pyplot as plt
import numpy as np
import sys

def flux_graph(TAPobject_data: TAPobject):

	fig2, ax2 = plt.subplots()

	ax2.set_xlabel('$Time\ (s)$', fontsize = 14)

	colors = ['b','orange','g','r','k','y','c','m','brown','darkgreen','goldenrod','lavender','lime']

	ax2.set_ylabel('$Concentration (mol/cm3)$', fontsize = 14)
	
	try:
		experimental_data = read_experimental_data_object(TAPobject_data.data_name)
		experimental_data_exist = True
	except:
		print('no experimental data')
		experimental_data_exist = False

	synthetic_data = read_experimental_data_object('./'+TAPobject_data.output_name+'/TAP_experimental_data.json')	
	
	legend_label = []
	for j in TAPobject_data.reactor_species.gasses:
		legend_label.append(j)
	for j in TAPobject_data.reactor_species.inert_gasses:
		legend_label.append(j)

	for jnum,j in enumerate(TAPobject_data.reactor_species.gasses):
		for k in synthetic_data[j]:
			plt.plot(synthetic_data['time'][0], synthetic_data[j][0],label=j,color=colors[jnum],linestyle='--')
			
	for jnum,j in enumerate(TAPobject_data.reactor_species.inert_gasses):
		for k in synthetic_data[j]:
			plt.plot(synthetic_data['time'][0], synthetic_data[j][0],label=j,color=colors[jnum+len(TAPobject_data.reactor_species.gasses.keys())],linestyle='--')		
	
	plt.xlim(0,synthetic_data['time'][0][-1])
	
	if experimental_data_exist == True:
		for jnum,j in enumerate(TAPobject_data.reactor_species.gasses):#
			for k in experimental_data[j]:
				plt.scatter(experimental_data['time'][0][::6], experimental_data[j][0][::6],s=5,label=j+'_exp',color=colors[jnum])
	
		for jnum,j in enumerate(TAPobject_data.reactor_species.inert_gasses):
			for k in experimental_data[j]:
				plt.scatter(experimental_data['time'][0][::6], experimental_data[j][0][::6],s=5,label=j+'_exp',color=colors[jnum+len(TAPobject_data.reactor_species.gasses.keys())])#


	plt.savefig('./flux_graph.pdf')
	plt.legend()
	plt.show()