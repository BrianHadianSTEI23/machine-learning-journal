
import sklearn.model_selection as sk
import pandas as pd
import sys

if __name__ == "__main__":

    # get the argument of how many fold (k)
    k : int = int(sys.argv[1])

    # import data from the dataset
    df = pd.read_csv("./data/bitcoin_data.csv") # read only

    # convert into numpy
    np_df = df.to_numpy()

    # partition it into k fold validation
    X_train, X_test, y_train, y_test = sk.train_test_split(np_df, test_size=float(1/k), random_state=42)

    # print result
    print("////////////// X train ////////////////")
    print(X_train)
    print("////////////// y train ////////////////")
    print(y_train)
    print("////////////// X test ////////////////")
    print(X_test)
    print("////////////// y test ////////////////")
    print(y_test)

    pass
