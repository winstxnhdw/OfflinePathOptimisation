# OFFLINE PATH PLANNING OPTIMISATION
This notebook elaborates the testing and development of an offline path planning optimisation pipeline to generate a safe and feasible reference path for a ego vehicle. The pipeline takes a set of coarsely placed waypoints and adjusts their localisation so as to comply with certain path curvature constraints in view of the vehicle's size and steering capability. The adjusted waypoints should be as close as possible to the original waypoints without violating the curvature constraints.

### Installation
Before beginning, it is important to install all the dependencies to run all cells in this notebook.

!pip install -r requirements.txt

### Imports


```python
import numpy as np
import pandas as pd
import scipy.interpolate as sp_interp
import scipy.optimize as optimize

from numba import njit
```

### Generating Waypoints
To easily generate waypoints for testing, we will use a modified version of my [Waypoint Generator](https://github.com/winstxnhdw/WaypointGenerator) script. The generated waypoints are exported as a CSV file and can be imported again using the pandas library.


```python
%matplotlib widget

import matplotlib.pyplot as plt

class ClickGenerator:

    def __init__(self, ax, fig, map_size, line_colour, point_colour):
        
        self.x = []
        self.y = []

        self.ax = ax
        self.fig = fig
        self.map_size = map_size
        self.line_colour = line_colour
        self.point_colour = point_colour

    def generate(self):

        def onclick(event):

            self.x.append(event.xdata)
            self.y.append(event.ydata)

            self.ax.plot(self.x, self.y, '-', color=self.line_colour)
            self.ax.plot(self.x, self.y, '.', color=self.point_colour)

            self.fig.canvas.draw()

            axis = {'X-axis': self.x, 'Y-axis': self.y}
            df = pd.DataFrame(axis, columns= ['X-axis', 'Y-axis'])
            df.to_csv("waypoints.csv", index = False)

        def onpress(event):

            # Undo last point
            if event.key == 'z':
                try:
                    self.x.pop()
                    self.y.pop()

                except:
                    pass
            
            # Clear all the points
            elif event.key == 'x':
                del self.x[:]
                del self.y[:]

            # Connect the first and last points
            elif event.key == 'c':
                try:
                    self.x.append(self.x[0])
                    self.y.append(self.y[0])

                except:
                    pass
        
            else:
                pass
        
            plt.cla()
            plt.grid()
            self.ax.set_xlim(-self.map_size, self.map_size)
            self.ax.set_ylim(-self.map_size, self.map_size)
            self.ax.plot(self.x, self.y, '-', color=self.line_colour)
            self.ax.plot(self.x, self.y, '.', color=self.point_colour)
            self.fig.canvas.draw()

            axis = {'X-axis': self.x, 'Y-axis': self.y}
            df = pd.DataFrame(axis, columns= ['X-axis', 'Y-axis'])
            df.to_csv("waypoints.csv", index = False)

        self.fig.canvas.mpl_connect('button_press_event', onclick)
        self.fig.canvas.mpl_connect('key_press_event', onpress)

def main():

    # Parameters
    map_size = 100
    line_colour = '#F0A39A'
    point_colour = '#383831'

    fig = plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-map_size, map_size)
    ax.set_ylim(-map_size, map_size)

    click_gen = ClickGenerator(ax, fig, map_size, line_colour, point_colour)
    click_gen.generate()

    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
```


    Canvas(toolbar=Toolbar(toolitems=[('Home', 'Reset original view', 'home', 'home'), ('Back', 'Back to previous …


!jupyter nbconvert main.ipynb --to markdown --output README.md
