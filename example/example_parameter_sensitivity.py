from batchsolver import *
import numpy as np
import os

jinwoo_forward = read_TAPobject('./jinwoo_model.json')

jinwoo_forward.parameters_of_interest = ['TAPobject_data.reactor_species.gasses["C3H8"].intensity','TAPobject_data.reactor_species.gasses["O2"].intensity','TAPobject_data.reactor_species.gasses["C3H8"].delay','TAPobject_data.reactor_species.gasses["O2"].delay','TAPobject_data.reactor_species.temperature']
jinwoo_forward.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
jinwoo_forward.output_name = 'fit_new'
jinwoo_forward.data_name = None
jinwoo_forward.finite_difference_trans_sensitivty = True

jinwoo_forward.reactor_species.gasses["C3H8"].intensity = 1.2 # Must be greater than 0 (can be continuous value)
jinwoo_forward.reactor_species.gasses["O2"].intensity = 0.8 # Must be greater than 0 (can be continuous value)
jinwoo_forward.reactor_species.gasses["C3H8"].delay = 0.3 # delay must be increment of 0.001 and greater than 0
jinwoo_forward.reactor_species.gasses["O2"].delay = 0.0 
jinwoo_forward.reactor_species.temperature = 675 # Generally keep between +/- 125 (can be continuous value)

jinwoo_updated = update_parameters(jinwoo_forward)
jinwoo_updated.output_name = 'exp_new'

transient_sensitivity(1,1,jinwoo_updated)

new_output = read_transient_sensitivity('./'+jinwoo_updated.output_name+'/TAP_test.json')
print(new_output)