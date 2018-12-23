import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
from subprocess import call


def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')


if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    prs.add_argument("-f", dest="file", required=True, help="The csv file to plot.\n")
    args = prs.parse_args()

    #plt.ylim([20,220])
    #plt.xlim([250,19800])
    #plt.axvline(x=10000, color='k', linestyle='--')

    df = pd.read_csv(args.file)

    plt.figure(1)
    plt.plot(df['step_time'], moving_average(df['total_stopped'], window_size=6))
    plt.title("")
    plt.xlabel("Time Step")
    plt.ylabel("Total Number of Stopped Vehicles")
    plt.grid()

    plt.figure(2)
    plt.plot(df['step_time'], moving_average(df['total_wait_time'], window_size=6))
    plt.title("")
    plt.xlabel("Time Step")
    plt.ylabel("Total Waiting Time of Vehicles")
    plt.grid()

    plt.figure(3)
    plt.plot(df['step_time'], moving_average(df['buffer_size'], window_size=6))
    plt.title("")
    plt.xlabel("Time Step")
    plt.ylabel("Buffer Size")
    plt.grid()

    plt.show()

