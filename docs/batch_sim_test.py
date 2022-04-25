from tapsolver import *
import numpy as np
import os

new_reactor = reactor()

### Add the reactor gasses (reactive and inert)
new_reactor_species = reactor_species()
new_reactor_species.reference_temperature = 700
new_reactor_species.temperature = 650

C3H8 = define_gas()
C3H8.intensity = 3.0
C3H8.delay = 0.0
C3H8.sigma = 0.1
C3H8.noise = 0.1
new_reactor_species.add_gas('C3H8',C3H8)

O2 = define_gas()
O2.intensity = 10.0
O2.delay = 0.0
O2.sigma = 0.1
O2.noise = 0.1
new_reactor_species.add_gas('O2',O2)
#
C3H6 = define_gas()
C3H6.intensity = 0.0
C3H6.delay = 0.0
C3H6.sigma = 0.1
C3H6.noise = 0.1
new_reactor_species.add_gas('C3H6',C3H6)

H2O = define_gas()
H2O.intensity = 0.0
H2O.delay = 0
H2O.sigma = 0.1
H2O.noise = 0.1#0.1
new_reactor_species.add_gas('H2O',H2O)

CO2 = define_gas()
CO2.intensity = 0.0
CO2.delay = 0.0
CO2.sigma = 0.1
CO2.noise = 0.1#0.1
new_reactor_species.add_gas('CO2',CO2)

Ar = define_gas()
Ar.intensity = 1
Ar.delay = 0.0
Ar.noise = 0#0.1
Ar.sigma = 0#0.1
new_reactor_species.add_inert_gas('Ar',Ar)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H8*',s)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('O*',s)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H6*',s)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H4*',s)

s = define_adspecies()
s.concentration = 480
new_reactor_species.add_adspecies('*',s)

new_mechanism = mechanism()

new_mechanism.elementary_processes[0] = elementary_process('C3H8 + * <-> C3H8*')
new_mechanism.elementary_processes[1] = elementary_process('O2 + 2* <-> 2O*')
new_mechanism.elementary_processes[2] = elementary_process('C3H6 + * <-> C3H6*')
new_mechanism.elementary_processes[3] = elementary_process('C3H8* + O* <-> C3H6* + H2O + *')
new_mechanism.elementary_processes[4] = elementary_process('C3H8* + 2O* <-> C3H4* + 2H2O + *')
new_mechanism.elementary_processes[5] = elementary_process('C3H6* + O* <-> C3H4* + H2O + *')
new_mechanism.elementary_processes[6] = elementary_process('C3H4* + 8O* <-> 3CO2 + 2H2O + 9*')

new_mechanism.elementary_processes[0].forward.dG = 0.3#-0.2
new_mechanism.elementary_processes[0].forward.Ga = 1.53
new_mechanism.elementary_processes[1].forward.dG = 0.3#-0.6
new_mechanism.elementary_processes[1].forward.Ga = 1.45
new_mechanism.elementary_processes[2].forward.dG = 0.3#0.2
new_mechanism.elementary_processes[2].forward.Ga = 0.25
new_mechanism.elementary_processes[3].forward.dG = -1
new_mechanism.elementary_processes[3].forward.Ga = 1.5#1.65
new_mechanism.elementary_processes[4].forward.dG = -3.98
new_mechanism.elementary_processes[4].forward.Ga = 1.5#1.45
new_mechanism.elementary_processes[5].forward.dG = -3.62
new_mechanism.elementary_processes[5].forward.Ga = 1.5#1.45
new_mechanism.elementary_processes[6].forward.dG = -8
new_mechanism.elementary_processes[6].forward.Ga = 0.1

new_mechanism.elementary_processes[3].forward.lower_bound = 1.2
new_mechanism.elementary_processes[3].forward.upper_bound = 2.2
new_mechanism.elementary_processes[4].forward.lower_bound = 1.2
new_mechanism.elementary_processes[4].forward.upper_bound = 2.2
new_mechanism.elementary_processes[5].forward.lower_bound = 1.2
new_mechanism.elementary_processes[5].forward.upper_bound = 2.2

## Make a function
for j in new_mechanism.elementary_processes:
	new_mechanism.elementary_processes[j].forward.use = 'G'
try:
	new_mechanism.elementary_processes[j].backward.use = 'G'
except:
	pass

mechanism_constructor(new_mechanism)

opdh_1 = TAPobject()
opdh_1.reactor = new_reactor
opdh_1.reactor_species = new_reactor_species
opdh_1.mechanism = new_mechanism

opdh_1.show_graph = False
opdh_1.parameter_scale = 480
opdh_1.output_name = 'exp_new'

### Step #1 - Run simulations

temp_gasses = opdh_1.reactor_species.gasses
temp_inert_gasses = opdh_1.reactor_species.inert_gasses
temp_adspecies = opdh_1.reactor_species.adspecies
temp_reactants = opdh_1.mechanism.reactants

#opdh_1.parameters_of_interest = ['TAPobject_data.reactor_species.gasses["C3H8"].intensity','TAPobject_data.mechanism.elementary_processes[1].forward.dG']
opdh_1.parameters_of_interest = ['TAPobject_data.mechanism.elementary_processes[0].forward.dG','TAPobject_data.mechanism.elementary_processes[1].forward.dG','TAPobject_data.mechanism.elementary_processes[2].forward.dG','TAPobject_data.mechanism.elementary_processes[3].forward.Ga','TAPobject_data.mechanism.elementary_processes[4].forward.Ga','TAPobject_data.mechanism.elementary_processes[5].forward.Ga']
opdh_1.output_name = 'fit_new'
opdh_1.data_name = None
opdh_1.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
#opdh_1.finite_difference_trans_sensitivty = True
#save_object(opdh_1,'./jinwoo_save/mech_1.json')
#transient_sensitivity(3,1,opdh_1)
#sys.exit()
print(opdh_1.mesh)
opdh_1.data_name = './exp_new/TAP_experimental_data.json'
opdh_1.output_name = 'fit_new'
opdh_1.optimize = True
forward_problem(0.5,1,opdh_1)
flux_graph(opdh_1)