from batchsolver import *
import numpy as np
import os

new_reactor = reactor()

### Add the reactor gasses (reactive and inert)
new_reactor_species = reactor_species()
new_reactor_species.reference_temperature = 700
new_reactor_species.temperature = 650

C3H8 = define_gas()
C3H8.mass = 44.1
C3H8.intensity = 1.0
C3H8.delay = 0.0
C3H8.sigma = 0.2
C3H8.noise = 0.2
new_reactor_species.add_gas('C3H8',C3H8)

O2 = define_gas()
O2.mass = 32
O2.intensity = 1.0
O2.delay = 0.0
O2.sigma = 0.2
O2.noise = 0.2
new_reactor_species.add_gas('O2',O2)
#
C3H6 = define_gas()
C3H6.mass = 42.08
C3H6.intensity = 0.0
C3H6.delay = 0.0
C3H6.sigma = 0.2
C3H6.noise = 0.2
new_reactor_species.add_gas('C3H6',C3H6)

H2O = define_gas()
H2O.mass = 18
H2O.intensity = 0.0
H2O.delay = 0
H2O.sigma = .2
H2O.noise = 0.2
new_reactor_species.add_gas('H2O',H2O)

CO2 = define_gas()
CO2.mass = 44.01
CO2.intensity = 0.0
CO2.delay = 0
CO2.sigma = .2
CO2.noise = .2
new_reactor_species.add_gas('CO2',CO2)

Ar = define_gas()
Ar.mass = 40.1
Ar.intensity = 1
Ar.delay = 0.0
Ar.noise = 0.2
Ar.sigma = 0.2
new_reactor_species.add_inert_gas('Ar',Ar)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H8*',s)

s = define_adspecies()
s.concentration = 240
new_reactor_species.add_adspecies('O*',s)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H6*',s)

s = define_adspecies()
s.concentration = 0
new_reactor_species.add_adspecies('C3H4*',s)

s = define_adspecies()
s.concentration = 240
new_reactor_species.add_adspecies('*',s)

new_mechanism = mechanism()

new_mechanism.elementary_processes[0] = elementary_process('C3H8 + * <-> C3H8*')
new_mechanism.elementary_processes[1] = elementary_process('O2 + 2* <-> 2O*')
new_mechanism.elementary_processes[2] = elementary_process('C3H6 + * <-> C3H6*')
new_mechanism.elementary_processes[3] = elementary_process('C3H8* + O* <-> C3H6* + H2O + *')
new_mechanism.elementary_processes[4] = elementary_process('C3H8* + 2O* <-> C3H4* + 2H2O + 2*')
new_mechanism.elementary_processes[5] = elementary_process('C3H6* + O* <-> C3H4* + H2O + *')
new_mechanism.elementary_processes[6] = elementary_process('C3H4* + 8O* <-> 3CO2 + 2H2O + 9*')

new_mechanism.elementary_processes[0].forward.k = 0.0001#0.02
new_mechanism.elementary_processes[0].backward.k = 0

new_mechanism.elementary_processes[1].forward.k = 0.0001#.0004
new_mechanism.elementary_processes[1].backward.k = 0.0

new_mechanism.elementary_processes[2].forward.k = 0.0
new_mechanism.elementary_processes[2].backward.k = 0.0001#1000

new_mechanism.elementary_processes[3].forward.k = 0.0001#1
new_mechanism.elementary_processes[3].backward.k = 0

new_mechanism.elementary_processes[4].forward.k = 0.0001#.01
new_mechanism.elementary_processes[4].backward.k = 0

new_mechanism.elementary_processes[5].forward.k = 0.0001#.06
new_mechanism.elementary_processes[5].backward.k = 0

new_mechanism.elementary_processes[6].forward.k = 1
new_mechanism.elementary_processes[6].backward.k = 0

for j in new_mechanism.elementary_processes:
    new_mechanism.elementary_processes[j].forward.use = 'k'
    try:
        new_mechanism.elementary_processes[j].backward.use = 'k'
    except:
        pass

mechanism_constructor(new_mechanism)

opdh_1 = TAPobject()
opdh_1.reactor = new_reactor
opdh_1.reactor_species = new_reactor_species
opdh_1.mechanism = new_mechanism

opdh_1.show_graph = False
#opdh_1.parameter_scale = 480
opdh_1.output_name = 'exp_new'

opdh_1.parameters_of_interest = ['TAPobject_data.mechanism.elementary_processes[0].forward.k','TAPobject_data.mechanism.elementary_processes[1].forward.k','TAPobject_data.mechanism.elementary_processes[2].backward.k','TAPobject_data.mechanism.elementary_processes[3].forward.k','TAPobject_data.mechanism.elementary_processes[4].forward.k','TAPobject_data.mechanism.elementary_processes[5].forward.k']
#opdh_1.data_name = './exp_new/TAP_experimental_data.json'
opdh_1.gasses_objective = ['C3H8','O2','C3H6','H2O','CO2']
#opdh_1.output_name = 'fit_new'
#opdh_1.optimize = True

opdh_1.output_name = 'exp_new'
opdh_1.data_name = None
opdh_1.finite_difference_trans_sensitivty = True

transient_sensitivity(2, 1, opdh_1)
#forward_problem(1,1,opdh_1)
#flux_graph(opdh_1)
