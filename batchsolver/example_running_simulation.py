from batchsolver import *
import numpy as np
import os

jinwoo_forward = read_TAPobject('./jinwoo_model.json')
jinwoo_forward.output_name = 'exp_new'
forward_problem(1,1,jinwoo_forward)