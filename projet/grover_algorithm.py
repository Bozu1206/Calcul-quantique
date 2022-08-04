# -*- coding: utf-8 -*-

# -- Sheet --

# initialization
import numpy as np
from qiskit import *
from qiskit import QuantumCircuit
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram

#Loading IBMQ account
#IBMQ.save_account("put your IBM Q token here")
provider = IBMQ.load_account()

n = 4
qc = QuantumCircuit(n, n - 1)

qc.x(3)
qc.barrier()
qc.h(range(0, 4))
qc.barrier()

### Oracle 
qc.toffoli(0, 2, 3)
qc.toffoli(1, 2, 3)
qc.barrier()

### Reflection 
qc.h(range(0, 3))
qc.barrier()
qc.x(range(0, 3))
qc.h(2)
qc.toffoli(0, 1, 2)
qc.h(2)
qc.x(range(0, 3))
qc.barrier()
qc.h(range(0, 3))

qc.measure(np.arange(0, 3), np.arange(0, 3))

qc.draw(output='mpl')

# Simulator 
aer_sim = Aer.get_backend('aer_simulator')
result = aer_sim.run(assemble(qc)).result()
answer = result.get_counts()
plot_histogram(answer)

# Real devices
backend = least_busy(provider.backends(filters=lambda x: 5 >= x.configuration().n_qubits>=2 
                                                       and not x.configuration().simulator 
                                                       and x.status().operational == True))

print ("least busy backend: ", backend)

from qiskit.tools.monitor import job_monitor
shots = 8192

transpiled_bv_circuit = transpile(qc, backend)
job = backend.run(transpiled_bv_circuit, shots=shots)
job_monitor(job, interval=2)

# Get the results from the computation
results = job.result()
answer = results.get_counts()
plot_histogram(answer)

# -- Sheet 2 --

# initialization
import numpy as np

# importing Qiskit
from qiskit.providers.ibmq import least_busy

from qiskit import * 

# import basic plot tools
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit

#Loading your IBM Q account(s)
#IBMQ.save_account("dcb2e2023aa2d3f9d93fa6ea1dbc4a80c1a8fa32474729b2d71e4cf05ac500dfdc0c686d1b8a5070ac105c05655cbd3df6c4a0707539ed076da311edf22ba49f")
provider = IBMQ.load_account()



from numpy import pi 

n = 3
qc = QuantumCircuit(n, n)

qc.barrier()
qc.h(range(0,3))
qc.barrier()

### Oracle 
qc.cp(pi/2, 1, 2)
qc.cp(pi/2, 2, 1)
qc.cp(pi/2, 2, 0)
qc.cp(pi/2, 0, 2)

qc.barrier()

### Reflection 
qc.h(range(0,3))
qc.barrier()
qc.x(range(0,3))
qc.h(2)
qc.toffoli(0,1,2)
qc.h(2)
qc.x(range(0,3))
qc.barrier()
qc.h(range(0,3))

qc.measure(np.arange(0,3), np.arange(0,3))


qc.draw(output='mpl')

# Simulator 
aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(qc)
result = aer_sim.run(qobj).result()
answer = result.get_counts()
plot_histogram(answer)

# Real devices
backend = least_busy(provider.backends(filters=lambda x: 5 >= x.configuration().n_qubits >= 2 
                                                       and not x.configuration().simulator 
                                                       and x.status().operational == True))

print ("least busy backend: ", backend)

from qiskit.tools.monitor import job_monitor
shots = 8192

transpiled_bv_circuit = transpile(qc, backend)
job = backend.run(transpiled_bv_circuit,shots=shots)
job_monitor (job, interval=2)

# Get the results from the computation
results = job.result()
answer = results.get_counts()
plot_histogram(answer)

