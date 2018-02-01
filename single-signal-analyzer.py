import os 
import sys
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

if __name__ == '__main__':

    SIGNAL_IDX = 1

    if SIGNAL_IDX < 1:
        sys.exit()

    # Get the CSV file. 

    dir_name = 'captured-signals' + os.sep + 'signals.csv'
    signals_file = pd.read_csv(dir_name, header=None)

    # Observe some basic information. 
    number_of_signals = len(signals_file.loc[:, 0])
    size_of_signal = len(signals_file.loc[0, :])
    print('Number of signals: %s\nSize of signal: %s datapoints' %(number_of_signals, size_of_signal))

    # Now, analyze each signal, one by one, and classify it. 
    # In the 101th column of the csv file, manually enter a 0 or 1. 
    # A 0 will signify that the data is not valid, and the opposite for a 1. 

    print('Observing signal #%s' %(SIGNAL_IDX))
    # Exclude the 101th column, or 100th index, because that is where I will be storing the classification. 
    individual_signal = signals_file.loc[SIGNAL_IDX - 1, 0:99]
    x = np.linspace(0, 100, 100)

    fig = plt.figure() 
    ax0 = fig.add_subplot(111)
    ax0.set_title('Signal #%s' %(SIGNAL_IDX))
    ax0.scatter(x, individual_signal)
    plt.show()