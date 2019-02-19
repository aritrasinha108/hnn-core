"""
===============
Simulate dipole
===============

This example demonstrates how to simulate a dipole using the Neuron
simulator.
"""

# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#          Sam Neymotin <samnemo@gmail.com>

import os.path as op

###############################################################################
# Let us import mne_neuron

import mne_neuron
from mne_neuron import simulate_dipole, Params

from neuron import h

###############################################################################
# Then we setup the directories and Neuron
mne_neuron_root = op.join(op.dirname(mne_neuron.__file__), '..')
h.load_file("stdrun.hoc")
h.nrn_load_dll(op.join(mne_neuron_root, "x86_64/.libs/libnrnmech.so"))

###############################################################################
# Then we read the parameters file
params_fname = op.join(mne_neuron_root, 'param', 'default.param')
params = Params(params_fname)
print(params)

###############################################################################
# Now let's simulate the dipole and plot it
dpl = simulate_dipole(params)
dpl.plot()
