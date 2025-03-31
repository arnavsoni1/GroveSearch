# GroveSearch

As we all know, Grover's algorithm is used for searchng in untructured databases, or similar problems. Theoretically, it is used to find solutions to an equation f(x) = 1 for a boolean function f(x). So, technically - if the quantum hardware meets the demand, Grover's algorithm could be a step-up from the classical algorithms used to solve exhaustive search problems. One such problem is the Steiner tree problem. 

GroveSearch is a project that solves (or atleast attempts to solve) the Steiner tree problem using the Grover's Algorithm by implementing it in Qiskit. 

First, we encode the edges of the graph as qubits, and quantum states as superpositions of edge subsets. Then, we use the oracle to flip the phase of valid states and the diffusion operator to invert the amplitudes. This second step is repeated about π/4 * sqrt(k), where k is the ratio number of possible edge subsets to the number of solutions. Then, we repeat initialization and search until convergence, altering the minimum_weight as we go. 
The successful execution of this program with maximum efficiency requires large-scale error corrected quantum computers, and based on current hardware, this program may not be 100% accurate, and classical methods such as the Dreyfus-Wagner approach, though theoretically more complex, have the upper hand due to minimal hardware requirements. 
