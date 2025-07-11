# Scientific Computing using Python - 1. Python and Scientific Computing (2025)

Project repository created by Marcell Fekete.

The repository carries code to solve the Lorenz attractor problem using an Euler solver and then visualise the solutions. For a full description of how to use the repository, see the section about [Usage](#usage).

## Installation

Clone the repository.

```
git clone https://github.com/vrmer/scientific_computing_1.git
```

Initialise the `conda` environment using the following command, then activate it.

```
conda env create -f environment.yaml
conda activate scientific_computing
```

Install the `euler_solver` package from the root directory of the repository.

```
pip install -e .
```

## Usage

To simply run the Euler solver, use one of the config files in the `configs` folder:

```
python main.py configs/case_1.toml
```

This provides the following parameters to the solver:

* $x = 0$
* $y = 1$
* $z = 1.05$
* $\sigma = 10$
* $\beta = 2.667$
* $\rho = 6$

Besides the five different hyperparameter cases, you can also provide alternative parameters to the Euler solver using a `toml` file like the ones provided in the `configs` folder.

Alternatively, you can directly provide initial values for the positions in the dimensions $\{x, y, z\}$ using arguments with flags to the `main.py` script, for example:

```
python main.py configs/case_1.toml -x 6 -y 2.337 -z -4
```

This replaces the values of $\{x, y, z\}$ from the provided config file with $\{6, 2.337, -4\}$.

When the `main.py` script is run with `configs/case_1.toml`, the full list of positions are saved in the `outputs/case_1` directory by default. Similarly, three 2D visualisations of the positions and a 3D visualisation are saved to the `figures/case_1` directory by default. The output filepaths can be overriden in the config files.

Finally, it is also possible to only visualise the points of a simulation in a 3d plot without actually saving it. For this, use the `--show_plot` flag.

## Testing

Running the `pytest` command carries out 7 tests in the `src/tests` directory. These cover the equations of the Euler solver, the output of the solver itself, and the way the Euclidean distance is calculated for the 2D visualisations.

## Directory structure

### `configs` directory

It contains the configuration files in the `toml` format that are used to input parameters to the Euler solver.

In all cases, $\{x, y, z\} = \{0, 1, 1.05\}$.

* `case_1.toml`
    * $\sigma = 10, \beta = \frac{8}{3}, \rho = 6$
* `case_2.toml`
    * $\sigma = 10, \beta = \frac{8}{3}, \rho = 16$
* `case_3.toml`
    * $\sigma = 10, \beta = \frac{8}{3}, \rho = 28$
* `case_4.toml`
    * $\sigma = 14, \beta = \frac{8}{3}, \rho = 28$
* `case_5.toml`
    * $\sigma = 14, \beta = \frac{13}{3}, \rho = 28$

### `figures` directory

It contains the figures generated from the various cases organised into separate directories per case. Each directory contains four files in the PDF format.

* `figure_3d.pdf` is the 3D representation of the Lorenz attractor.
* `figure_xy.pdf`, `figure_xz.pdf` and `figure_yz.pdf` all represent the 2D representations of the Lorenz attractor with dimensions $\{x, y\}$, $\{x, z\}$ and $\{y, z\}$, respectively.

### `outputs` directory

It contains the arrays of the positions in the Lorenz attractor per dimension as created by the Euler solver in the `.npz` format, one for each case.

### `src` directory

It contains the source files of the repository in its subfolder, the `euler_solver`, as well as test files.

##### `euler_solver` directory

This subfolder is also a package that can be installed following the instructions in the section about [Installation](#installation).

* `__init__.py`
* `equations.py`: functions corresponding to each of the three equations of the Euler solver
* `parameters.py`: dataclass with the necessary parameters of the Euler solver
* `solver.py`: implementation of the Euler solver
* `utils.py`: helper functions for:
    * saving and loading arrays
    * calculating the Euclidean distance between points of two arrays
    * implementing line colouring to illustrate the Euclidean distance in the visualisations
    * allow for parameters in the config file to fill the parameters of the dataclass in `parameters.py`
* `visualise.py`: functions for visualising 2 dimensions in 2D plots and 3 dimensions in 3D plots

##### `tests` directory

* `equation_test.py`: tests that the equations of the solver work properly
* `solver_test.py`: tests that the Euler solver returns the right shape and type of output
* `utils_test.py`: tests that the Euclidean distance implementation returns the right type and value

### `.gitignore`

Files and directories to be ignored by the GitHub repository.

### `chatgpt.py`

Programming solution provided by ChatGPT responding to the following prompt:

> Given parameters x, y, z and sigma, beta, and rho, suggest a full working solution in Python for using Euler's method for solving the ODE of a Lorenz attractor.

### `environment.yaml`

YAML file to initialise the conda environment from, for installation, see the section [Installation](#installation).

### `lorenz.ipynb`

Jupyter notebook where the testing of some functions was carried out in.

### `main.py`

The main script of the repository (see [Usage](#usage)).

### `setup.py`

It installs the `euler_solver` package (see [Installation](#installation)).


