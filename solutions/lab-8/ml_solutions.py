import numpy as np
import sklearn

def load_dataset_regression(filename):
    """
    Loads the dataset from the file. Shuffles it, then
    adds it to NumPy matrices.

    Input:
    filename - the name of a .csv file to load.

    Output:
    X, Y - NumPy arrays extracted from the .csv file. X is
           the data, Y is the labels.
    """
    # The skiprows=1 argument skips the first row, where the data labels are
    with open(filename, "r") as f:
        dataset = np.loadtxt(f, delimiter=",", skiprows=1)

    # Shuffle the dataset before splitting into train, validation, and test sets - this is
    # important to ensure an even distribution of datapoints in the train, validation,
    # and test sets.
    np.random.shuffle(dataset)

    # X is all columns except the "csMPa" column
    X = dataset[:,:-1]
    # Y is the "csMPa" column
    Y = dataset[:,-1]
    return X, Y

def split_data(X, Y):
    X_train = X[:round(X.shape[0]*0.8),:]
    X_valid = X[round(X.shape[0]*0.8):round(X.shape[0]*0.9),:]
    X_test = X[round(X.shape[0]*0.9):,:]

    Y_train = Y[:round(Y.shape[0]*0.8)]
    Y_valid = Y[round(Y.shape[0]*0.8):round(Y.shape[0]*0.9)]
    Y_test = Y[round(Y.shape[0]*0.9):]

    return X_train, Y_train, X_valid, Y_valid, X_test, Y_test


def least_squares_linear_regression(X_train, Y_train, X_valid, Y_valid):
    """
    Run least squares regression on the training set. Print out the loss. Then
    run a series of examples showing predictions and their true values.

    Input:
    X_train, Y_train, X_valid, Y_valid - NumPy arrays representing the
                                         training and validation sets.

    Output:
    None
    """
    thetas = np.linalg.lstsq(X_train, Y_train, rcond=None)
    print("Loss: {}".format(np.sqrt(np.sum(np.square( np.dot(X_train, thetas[0]) - Y_train )))))

    predictions = np.dot(X_valid, thetas[0])
    print(np.concatenate((Y_valid.reshape(Y_valid.shape[0], 1), predictions.reshape(predictions.shape[0], 1)), axis=1))


def feature_selection_least_squares(X_train, Y_train, X_valid, Y_valid):
    """
    Perform feature selection to construct a new X_train, X_valid using a
    function and feature of your choice. Then run least squares on the new
    X_train, Y_train, and make predictions on the new X_valid and the Y_valid.
    
    Print out the loss from running least squares without feature selection
    (so running it on the old X_train, X_valid), and the loss from running
    least squares with feature selection. Can you select functions which 
    reduce the accuracy below that of a linear model without feature selection?
    
    (If so - super cool!! If not - what might this tell you about the dataset?)
    
    Input:
    X_train, Y_train, X_valid, Y_valid - NumPy arrays representing the
                                         training and validation sets.

    Output:
    None - prints out validation loss with and without feature selection.
    """
    # This solution implements a logarithmic feature in the BMI column - answers may vary.
    BMI_col_train_log = np.log(X_train[:,2])
    BMI_col_valid_log = np.log(X_valid[:,2])

    X_train = np.concatenate((X_train, BMI_col_train_log[:,None]), axis=1)
    X_valid = np.concatenate((X_valid, BMI_col_valid_log[:,None]), axis=1)

    return least_squares_linear_regression(X_train, Y_train, X_valid, Y_valid)

from sklearn.neural_network import MLPRegressor

def NN_regressor(X_train, Y_train, X_valid, Y_valid):
    """
    Trains a neural network to perform regression on the dataset. Makes predictions
    on the validation set, and prints out the validation loss from a least squares
    regression versus that of the neural network regression.

    Input:
    X_train, Y_train, X_valid, Y_valid - NumPy arrays representing the
                                         training and validation sets.
    
    Output:
    None - prints out validation loss of NN and least squares regression.
    """
    clf = MLPRegressor(hidden_layer_sizes=(32, 64, 128, 64, 32), learning_rate_init=0.0008, max_iter=400, verbose=True).fit(X_train, Y_train)

    predictions = clf.predict(X_valid)
    print(np.concatenate((Y_valid.reshape(Y_valid.shape[0], 1), predictions.reshape(predictions.shape[0], 1)), axis=1))

    print("NN Valiation Loss: {}".format(np.sqrt(np.sum(np.square( predictions - Y_valid )))))

def NN_regressor_test(X_train, Y_train, X_test, Y_test):
    """
    When you feel like you're doing a pretty good job on your validation set, try
    training your neural network on the training set, then running your neural 
    network on the test set! Print out yuor predictions and the true test set values.
    How close are your predictions?
    
    Remember that we use the test set once - and only once - to remove experimenter
    bias in the process. In this way, experimentors can't tune their hyperparameters
    to ensure a good fit on the test set, when in reality, their model may fail to
    generalize to new example cases that come in.
    
    Input:
    X_train, Y_train, X_test, Y_test - NumPy arrays representing the
                                       training and test sets.
    
    Output:
    None - prints out test labels and predictions.
    """
    clf = MLPRegressor(hidden_layer_sizes=(32, 64, 128, 64, 32), learning_rate_init=0.0008, max_iter=400, verbose=True).fit(X_train, Y_train)

    predictions = clf.predict(X_test)
    predictions = clf.predict(X_valid)
    print(np.concatenate((Y_test.reshape(Y_test.shape[0], 1), predictions.reshape(predictions.shape[0], 1)), axis=1))

    print("NN Test Loss: {}".format(np.sqrt(np.sum(np.square( predictions - Y_test )))))
