import numpy as np

class Spline:

    def __init__(self, x, y):
        pass

    def solve(self):
        pass

    def solve_1st_derivation(self):
        pass

    def solve_2nd_derivation(self):
        pass

class Spline2D:

    def __init__(self):
        pass

def generate_cubic_path(x, y, ds=0.05):

    spline = Spline(x, y)

    return px, py, pyaw, pk

def main():
    
    import pandas as pd
    import matplotlib.pyplot as plt

    dir_path = 'data/waypoints.csv'
    df = pd.read_csv(dir_path)
    x = df['X-axis'].values.tolist()
    y = df['Y-axis'].values.tolist()
    ds = 0.05

    px, py, pyaw, pk = generate_cubic_path(x, y, ds)

    figure = plt.figure()
    ax = plt.axes()
    ax.plot(x, y, '-o')
    ax.plot(px, py)
    plt.show()

if __name__ == '__main__':
    main()