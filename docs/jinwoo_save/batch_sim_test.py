from tapsolver import *
import numpy as np
import os

opdh_1 = read_TAPobject('./mech_1.json')

opdh_1.parameters_of_interest = ['TAPobject_data.reactor_species.gasses["C3H8"].intensity','TAPobject_data.mechanism.elementary_processes[1].forward.dG']
#opdh_1.parameters_of_interest = ['TAPobject_data.mechanism.elementary_processes[0].forward.dG','TAPobject_data.mechanism.elementary_processes[1].forward.dG','TAPobject_data.mechanism.elementary_processes[2].forward.dG','TAPobject_data.mechanism.elementary_processes[3].forward.Ga','TAPobject_data.mechanism.elementary_processes[4].forward.Ga','TAPobject_data.mechanism.elementary_processes[5].forward.Ga']
opdh_1.output_name = 'exp_new'
opdh_1.data_name = None
opdh_1.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
opdh_1.finite_difference_trans_sensitivty = True
#save_object(opdh_1,'./jinwoo_save/mech_1.json')
transient_sensitivity(1,1,opdh_1)
#sys.exit()
forward_problem(0.5,1,opdh_1)
flux_graph(opdh_1)
