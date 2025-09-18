# About ai

`ai` is a Python framework about network of connected neurons.
Each neuron is a function with inputs and an output.
Connections between compatible types can be allowed, i.e., a neuron with an int output can connect to another with an int input.
`learn` function uses an A* algorithm to target a value.

Here are some test files for example:
- **hello_world.py**: This adds functions related to str and searches for connections translating the relationship x + y + z from input values, and shows the generalization with a user value.
- **test_ai1.py**: This adds functions related to numbers and str and displays connections for the number 103.
- **test_ai2.py**: This adds functions related to int and displays all possible connections starting from the number 18.
- **test_ai3.py**: This adds functions related to int and searches for connections translating the relationship x * y + z from input values ​​(chosen to be unambiguous), and shows the generalization with user values.
- **test_ai4.py**: This adds functions related to np.ndarray and searches for connections translating the relationship x * y + z from input values, and shows the generalization with user values.
- **test_full_ai.py**: This adds functions related to all the available types (currently implemented in any case) and activate certain types of neurons depending on the case with the display of connections of numbers between 100 and 999 or all possible connections of depth 2
- **test_number.py**: The goal is to find the connection from elementary bricks to form any number. Learning takes about 20 seconds for a total of 147 neurons.
- **test_expression.py**: The goal is to find the connection from elementary bricks to form any expression. After learning the numbers, learning takes about 30 seconds for a total of 193 neurons.

A basic GUI (**gui.py**) is available to manipulate a model. It is possible to visualize neurons graph in 2D or 3D, with colors.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2e62da84-a2a3-4431-96fa-c5e5c6a33c21" />
<img width="1853" height="903" alt="newplot" src="https://github.com/user-attachments/assets/8516ad6b-7c4f-4d6a-8f77-fcdd060d8bd4" />

# conda
```
conda create --name gt -c conda-forge graph-tool
conda activate gt
```

# pip
```
pip install colour
pip install dill
pip install matplotlib
pip install numpy
pip install pandas
pip install plotly
pip install pyqtgraph
pip install pyside6
pip install sympy
pip install textdistance
```
