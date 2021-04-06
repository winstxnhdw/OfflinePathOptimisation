import matplotlib.pyplot as plt
import pandas as pd

from libs.cubic_spline_planner import calc_spline_course

def main():

    dir_path = 'data/waypoints.csv'
    df = pd.read_csv(dir_path)
    x = df['X-axis'].values.tolist()
    y = df['Y-axis'].values.tolist()
    ds = 0.05

    px, py, pyaw, pk = calc_spline_course(x, y, ds)

    figure = plt.figure()
    ax = plt.axes()
    ax.plot(x, y, '-o')
    ax.plot(px, py)
    plt.show()

if __name__ == '__main__':
    main()