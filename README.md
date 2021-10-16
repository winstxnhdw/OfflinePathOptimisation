# OFFLINE PATH PLANNING OPTIMISATION

This notebook elaborates the testing and development of an offline path planning optimisation pipeline to generate a safe and feasible reference path for a ego vehicle. The pipeline takes a set of coarsely placed waypoints and adjusts their localisation so as to comply with certain **path curvature** constraints in view of the vehicle's size and steering capability. The adjusted waypoints should be as close as possible to the original waypoints without violating the curvature constraints.

<div align="center">
	<img src="resources/vis.gif" />
</div>

## Approaches

- [Focused Trajectory Planning for Autonomous On-Road Driving](https://www.ri.cmu.edu/pub_files/2013/6/IV2013-Tianyu.pdf) by Gu et. al.

- [Segmented Constrained Path Optimisation](examples/constrained.ipynb)

- [Unconstrained Waypoint Optimisation](examples/unconstrained.ipynb)

- [Controlled Unconstrained Waypoint Optimisation](examples/controlled.ipynb)

## Results

A controlled real-world test was conducted only on the waypoints which were generated from the [unconstrained approach](examples/unconstrained.ipynb). Empirical data displayed a more comfortable and human-like ride when compared to the tracking of unoptimised waypoints. When curb information is accounted for, in the [controlled approach](examples/controlled.ipynb), the resultant path was able to maintain a safer distance from the curb without any noticeable loss in passenger comfort.

## Requirements

```bash
# Python 3.9.5
$ pip install -r requirements.txt
```

## Issues

It is important that you adhere to versions stated in `requirements.txt` and install Python 3.9.5. Later versions of NumPy has shown to break the path optimiser.
