from batchsolver import *
import numpy as np
import os

jinwoo_forward = read_TAPobject('./jinwoo_model.json')

jinwoo_forward.parameters_of_interest = ['TAPobject_data.mechanism.elementary_processes[0].forward.k','TAPobject_data.mechanism.elementary_processes[1].forward.k','TAPobject_data.mechanism.elementary_processes[2].backward.k','TAPobject_data.mechanism.elementary_processes[3].forward.k']
jinwoo_forward.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
jinwoo_forward.output_name = 'fit_new'
jinwoo_forward.data_name = None
jinwoo_forward.finite_difference_trans_sensitivty = True

jinwoo_updated = update_parameters(jinwoo_forward)
jinwoo_updated.output_name = 'exp_new'

transient_sensitivity(1,1,jinwoo_updated)

# access transient data
new_output = read_transient_sensitivity('./'+jinwoo_updated.output_name+'/TAP_test.json')
