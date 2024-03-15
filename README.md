# Matrix Multiplication Test Assignment

**This is a simple project that includes:**
- **C++** code for calculating the matrix product of two 2D matrices.
- **CMake** instructions for building the C++ code.
- A **Python** wrapper for using the binary file within the Python environment and testing it.
- A set of **pytest** tests for checking the binary file's functionality.

## Requirements

- `Python` v3.10 or higher
- `CMake`

## Running Instructions

The instructions below are for Unix machines. To run on Windows, some modifications will be required.

### Building source files
```bash
mkdir build
cd build
cmake ..
make
cd -
```

### Setup python environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Run tests
```
pytest -v tests.py
```

## Known Weaknesses

- The use of certain tools: **CMake**, **pytest** `parametrize`, and `fixtures` is excessive for a project of this scale and was employed for demonstration purposes.
- The matrix multiplication function does not check the matrices for correct shape: theoretically, a matrix with different numbers of columns in different rows can be input. Solving this problem is straightforward but time-consuming, so this check and its testing are omitted here.
- This matrix multiplication function was implemented for `int` types only for demonstration purposes. In a real program, the choice of data types accepted by the function should be based on usage conditions and considerations of computation time and memory usage optimization.
- A part of the input data correctness tests was implemented on the **Python** side. This is a poor decision for several reasons: _Type Safety, Performance, Error Handling and Debugging_ and _Portability_. However, this decision is dictated by the architecture required in the assignment (see the next point) and the extreme complexity of performing some checks in **C++**.
- The format of interaction with the binary file - through standard input and output - is highly universal but at the same time not optimal. The next section suggests a more appropriate way to interact with **Python** code.

## Improvement Suggestions

- Move away from using standard input and output for interaction with the **C++** module. The simplest way is to use **PyBind11** for binding. A more complex, but reliable method - write code directly in **Cython**.
- Using **SWIG** to generate wrapper code that facilitates the interaction between **Python** and **C++** can improve development time.
- Packaging the module with **setuptools** will simplify the build process for the user, delegating it to the package manager. Such a package can then be distributed locally or via **PyPi**.
- If the project is not a set of tools for the developer but an executable program, it should be containerized, for example, using **Docker**.
