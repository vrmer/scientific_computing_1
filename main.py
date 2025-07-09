import os
import argparse
import tomllib
from src import (filter_to_dataclass, Parameters,
                 euler_solver, plot_2d_arrays, plot_3d_arrays)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="""Config with parameters for the 
        Euler solver of the Lorenz attractor""")
    
    parser.add_argument("config", help="Input toml file containing all necessary parameters.")
    parser.add_argument("-x", help="Optional x dimension input", type=float, required=False)
    parser.add_argument("-y", help="Optional y dimension input", type=float, required=False)
    parser.add_argument("-z", help="Optional z dimension input", type=float, required=False)
    parser.add_argument("--show_plot", 
                        help="If used, the plots are not saved and the 3d plot is shown instead",
                        action="store_true")
    
    args = parser.parse_args()
    
    # load parameters
    with open(args.config, "rb") as f:
        config = tomllib.load(f)
        
    params = filter_to_dataclass(Parameters, config)
    
    # optionally override x, y, z dimensions
    params.x = args.x if args.x else params.x
    params.y = args.y if args.y else params.y
    params.z = args.z if args.z else params.z

    # create the output directories and paths
    os.makedirs(config["position_dir"], exist_ok=True)
    os.makedirs(config["figures_dir"], exist_ok=True)

    positions_path = os.path.join(config["position_dir"], 
                                "positions.npz")

    # run the Euler solver
    euler_solver(params, positions_path)
    print("\nEuler solver complete.\n")

    # visualise all possible 2d plots
    # x and y
    output_path_xy = os.path.join(config["figures_dir"],
                                "figure_xy.pdf")
    if args.show_plot:
        pass
    else:
        plot_2d_arrays(target_path=positions_path,
                    dimensions=("x", "y"),
                    output_path=output_path_xy)
    # y and z
    output_path_yz = os.path.join(config["figures_dir"],
                                "figure_yz.pdf")
    if args.show_plot:
        pass
    else:
        plot_2d_arrays(target_path=positions_path,
                    dimensions=("y", "z"),
                    output_path=output_path_yz)
    # x and z
    output_path_xz = os.path.join(config["figures_dir"],
                                "figure_xz.pdf")
    if args.show_plot:
        pass
    else:
        plot_2d_arrays(target_path=positions_path,
                    dimensions=("x", "z"),
                    output_path=output_path_xz)
    
    # visualise the 3d plot
    output_path_3d = os.path.join(config["figures_dir"],
                            "figure_3d.pdf")
    if args.show_plot:
        plot_3d_arrays(target_path=positions_path)
    else:
        plot_3d_arrays(target_path=positions_path, output_path=output_path_3d)
    print("\nVisualisations complete.\n")
