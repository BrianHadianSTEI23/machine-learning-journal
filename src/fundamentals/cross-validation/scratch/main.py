
import sys 
import pandas as pd
import numpy as np

if __name__ == "__main__" : 

    # get the argument of how many fold (k)
    k : int = int(sys.argv[1])

    # import data from the dataset
    df = pd.read_csv("./data/bitcoin_data.csv") # read only

    # get how many data needed for the test
    n_test_data : int = (len(df) // k) + 1 # round upwards

    # do shuffle
    df_shuffle = df.sample(frac=1).reset_index(drop=True)

    # partition the data
    test_data = df_shuffle[:n_test_data]
    train_data = df_shuffle[n_test_data:]

    # partition into each and convert to numpy
    y_test = test_data[["Market Cap"]].to_numpy()
    X_test = test_data.drop("Market Cap", axis=1).to_numpy()
    y_train = train_data[["Market Cap"]].to_numpy()
    X_train = train_data.drop("Market Cap", axis=1).to_numpy()

    # split the data into x and y
