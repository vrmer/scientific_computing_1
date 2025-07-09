# Scientific Computing using Python - 1. Python and Scientific Computing (2025)

Project repository created by Marcell Fekete.

The repository carries code to solve the Lorenz attractor problem using an Euler solver and then visualise the solutions. For a full description of how to use the repository, see the section [Usage](#usage).

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

Running the `pytest` command carries out 7 tests in the `tests` directory. These cover the equations of the Euler solver, the output of the solver itself, and the way the Euclidean distance is calculated for the 2D visualisations.

## Directory structure


