# OFFLINE PATH PLANNING OPTIMISATION
This notebook elaborates the testing and development of an offline path planning optimisation pipeline to generate a safe and feasible reference path for a ego vehicle. The pipeline takes a set of coarsely placed waypoints and adjusts their localisation so as to comply with certain **path curvature** constraints in view of the vehicle's size and steering capability. The adjusted waypoints should be as close as possible to the original waypoints without violating the curvature constraints.

<div align="center">
	<img src="resources/vis.gif" />
</div>

## Installation
### Package Installer for Python
```bash
$ pip install -r requirements.txt
```

### Anaconda
```bash
$ conda create --name <env> --file conda_requirements.txt
```

### Convert PNG sequence to GIF (ImageMagick)
```bash
$ convert -delay 1x60 visualisation_*.png -loop 0 -background white -alpha remove vis.gif

```