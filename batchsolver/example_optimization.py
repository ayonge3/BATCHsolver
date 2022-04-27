from batchsolver import *
import numpy as np
import os

jinwoo_forward = read_TAPobject('./jinwoo_model.json')

jinwoo_forward.mechanism.elementary_processes[0].forward.k = 0.0001
jinwoo_forward.mechanism.elementary_processes[1].forward.k = 0.0001
jinwoo_forward.mechanism.elementary_processes[2].backward.k = 0.0001
jinwoo_forward.mechanism.elementary_processes[3].forward.k = 0.0001

jinwoo_forward.parameters_of_interest = ['TAPobject_data.mechanism.elementary_processes[0].forward.k','TAPobject_data.mechanism.elementary_processes[1].forward.k','TAPobject_data.mechanism.elementary_processes[2].backward.k','TAPobject_data.mechanism.elementary_processes[3].forward.k']
jinwoo_forward.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
jinwoo_forward.output_name = 'fit_new'
jinwoo_forward.optimize = True
jinwoo_forward.data_name = './exp_new/TAP_experimental_data.json'

forward_problem(1,1,jinwoo_forward)
