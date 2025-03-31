from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import GroverOptimizer
from qiskit_optimization.translators import from_docplex_mp
from docplex.mp.model import Model
from qiskit.primitives import Sampler

def create_steiner_qubo(graph, terminals):
    model = Model()
    edges = {e: model.binary_var(name=f'e{i}') for i, e in enumerate(graph.edges)}
    objective = sum(data['weight'] * var for (u, v, data), var in zip(graph.edges(data=True), edges.values()))
    penalty_strength = 2 * sum(data['weight'] for _, _, data in graph.edges(data=True))
    for i in range(len(terminals)-1):
        for j in range(i+1, len(terminals)):
            path_vars = [edges[e] for e in graph.edges if terminals[i] in e and terminals[j] in e]
            if path_vars:  
                model.add_constraint(
                    model.sum(path_vars) >= 1, 
                    f'conn_{terminals[i]}_{terminals[j]}'
                )
    qp = from_docplex_mp(model)
    from qiskit_optimization.converters import QuadraticProgramToQubo
    qp = QuadraticProgramToQubo(penalty=penalty_strength).convert(qp)
    return qp

def solve_steiner_grover(graph, terminals):
    qp = create_steiner_qubo(graph, terminals)
    grover = GroverOptimizer(
        num_value_qubits=6,
        num_iterations=3,
        sampler=Sampler()
    )
    quantum_result = grover.solve(qp)
    return quantum_result


   
