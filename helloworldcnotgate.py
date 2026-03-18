# from qiskit import QuantumCircuit
# from qiskit.quantum_info import SparsePauliOp
# from qiskit.transpiler import generate_preset_pass_manager
# from qiskit_ibm_runtime import EstimatorV2 as Estimator
# from qiskit_ibm_runtime.fake_provider import FakeBelemV2
# from matplotlib import pyplot as plt

# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0,1)
# print(qc.draw())

# observables_labels = ["IZ","IX","ZI","XI","ZZ","XX"]
# observables = [SparsePauliOp(label) for label in observables_labels]

# backend = FakeBelemV2()
# estimator = Estimator(backend)

# pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
# isa_circuit = pm.run(qc)

# mapped_observables = [obs.apply_layout(isa_circuit.layout) for obs in observables]

# job = estimator.run([(isa_circuit, mapped_observables)])
# job_result = job.result()
# pub_result = job_result[0]

# values = pub_result.data.evs
# errors = pub_result.data.stds

# plt.plot(observables_labels, values, "-o")
# plt.xlabel("Observables")
# plt.ylabel("Expectation Values")
# plt.show()



from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create a Quantum Circuit (1 qubit, 1 classical bit)
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure
qc.measure(0, 0)

# Get simulator
simulator = Aer.get_backend("qasm_simulator")

# Transpile and run
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)

# Get results
result = job.result()
counts = result.get_counts()

print("Measurement Result:", counts)
print(qc.draw())