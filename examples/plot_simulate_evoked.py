"""
===============
Simulate dipole
===============

This example demonstrates how to simulate a dipole for evoked-like
waveforms using HNN-core.
"""

# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#          Sam Neymotin <samnemo@gmail.com>

import os.path as op

###############################################################################
# Let us import hnn_core

import hnn_core
from hnn_core import simulate_dipole, read_params, Network

hnn_core_root = op.join(op.dirname(hnn_core.__file__), '..')

###############################################################################
# Then we read the parameters file
params_fname = op.join(hnn_core_root, 'param', 'default.json')
params = read_params(params_fname)
print(params)

###############################################################################
# This is a lot of parameters! We can also filter the
# parameters using unix-style wildcard characters
print(params['L2Pyr_soma*'])

###############################################################################
# Now let's simulate the dipole
# You can simulate multiple trials in parallel by using n_jobs > 1
net = Network(params)
dpls = simulate_dipole(net, n_jobs=1, n_trials=2)

###############################################################################
# and then plot it
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
for dpl in dpls:
    dpl.plot(ax=axes[0], layer='agg')
net.plot_input(ax=axes[1])

###############################################################################
# Finally, we can also plot the spikes.
net.plot_spikes()

###############################################################################
# Now, let us try to make the exogenous driving inputs to the cells
# synchronous and see what happens

params.update({'sync_evinput': True})
net_sync = Network(params)
dpls_sync = simulate_dipole(net_sync, n_jobs=1, n_trials=1)
dpls_sync[0].plot()
net_sync.plot_input()
