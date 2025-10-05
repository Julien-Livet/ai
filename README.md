# About ai

`ai` is a Python framework about network of connected neurons.
Each neuron is a function with inputs and an output.
Connections between compatible types can be allowed, i.e., a neuron with an int output can connect to another with an int input.
`learn` function uses an A* algorithm to target a value.
To run, `ai` requires a maximum of 500MB of RAM, runs on a CPU rather than a GPU, is deterministic, and is explainable. A model can fit on a few MB.

Here are some test files for example:
- **hello_world.py**: This adds functions related to str and searches for connections translating the relationship x + y + z from input values, and shows the generalization with a user value.
- **test_ai1.py**: This adds functions related to numbers and str and displays connections for the number 103.
- **test_ai2.py**: This adds functions related to int and displays all possible connections starting from the number 18.
- **test_ai3.py**: This adds functions related to int and searches for connections translating the relationship x * y + z from input values ​​(chosen to be unambiguous), and shows the generalization with user values.
- **test_ai4.py**: This adds functions related to np.ndarray and searches for connections translating the relationship x * y + z from input values, and shows the generalization with user values.
- **test_full_ai.py**: This adds functions related to all the available types (currently implemented in any case) and activate certain types of neurons depending on the case with the display of connections of numbers between 100 and 999 or all possible connections of depth 2
- **test_number.py**: The goal is to find the connection from elementary bricks to form any number.
- **test_expression.py**: The goal is to find the connection from elementary bricks to form any expression.
- **test_word.py**: This example aims to reconstruct French words from syllables.
- **test_sentence.py**: This example aims to reconstruct simple sentences from words.
- **test_sympy.py**: This example aims to find the symbolic transformation between an input expression and an output expression.
- **test_cv2.py**: This example aims to find the transformation between an input image and an output image.
- **test_syracuse.py**: This example aims to find the Syracuse sequence from intermediate steps.

A basic GUI (**gui.py**) is available to manipulate a model. It is possible to visualize neurons graph in 2D or 3D, with colors.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2e62da84-a2a3-4431-96fa-c5e5c6a33c21" />
<img width="1853" height="903" alt="newplot" src="https://github.com/user-attachments/assets/8516ad6b-7c4f-4d6a-8f77-fcdd060d8bd4" />

# Comparative benchmark

| Task | My engine (CPU) | LLM (estimated, API/GPU) | Comment |
|------------------------|------------------|------------------------|-------------|
| **Simple numeric** (e.g., `2+3`) | 0.01 s ✅ | ~1 s ⚠️ | Instantaneous and exact, against API latency and trivial error risk. |
| **Complex numeric** (e.g., `3.1*x + y`) | 0.01 s ✅ | ~1–2 s ⚠️ | Constant time, explainable; LLM can yield an equivalent but not necessarily identical expression. |
| **Symbolic diff** (e.g., differentiating `sin(x)*exp(x)`) | 0.70 s ✅ | ~2–5 s ❌ | Exact and explainable results. LLMs often hallucinate or fail. |
| **Word reconstruction** (e.g., reconstructing a word from syllables) | 0.11 s ✅ | ~1–3 s ❌ | Deterministic and reproducible; an LLM generates variants that are not guaranteed. |

✅ = exact and deterministic
⚠️ = depends on probabilistic generation
❌ = results often false or inconsistent

# conda
```
conda create --name gt -c conda-forge graph-tool
conda activate gt
```

# pip
```
pip install bs4
pip install colour
pip install dill
pip install matplotlib
pip install numpy
pip install pandas
pip install plotly
pip install pyqtgraph
pip install pyside6
pip install requests
pip install sympy
pip install textdistance
```

# The core algorithm

The main function is `learn` of `brain.py` script.
Here are the different steps:
- We first filter the activated connections
- We look at the activated leaf neurons (those with no inputs) and the cost corresponding to the objective
- We record the cost of the best connection
- We create two lists, one for the activated leaf neurons and another for the activated other neurons
- We sort the two lists in descending order of weights
- We initialize the `frontier` list with the leaf neurons
- We check that the path has not already been visited
- We establish the `av` list of available leaf neurons and connections
- We set this list to unique values
- We iterate over the non-leaf neurons
	- We keep the `av` types compatible with the inputs of the neuron in question
	- We iterate over all possible combinations of inputs
	- We calculate the output on the valid combinations
	- We create a new connection, calculate the cost, and add this path to the list managed by the A* algorithm

At the end, we strengthen the connections found and transform the connection that gives the exact result into neurons as needed.
We add the found connections to the brain.
