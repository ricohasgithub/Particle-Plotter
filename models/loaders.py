
import numpy as np
import pandas

import bz2, pickle
import matplotlib as plt

class DataLoader():

    def __init__(self):
        pass

class EventLoader(DataLoader):

    def __init__(self, filename, padded_size):

        self.data = pickle.load(bz2.BZ2File(filename, "r"))

        Xs = []
        ys = []

        for X, y in self.data:
            X = X[:padded_size]
            y = y[:padded_size]
            X = np.pad(X, ((0, padded_size - X.shape[0]), (0,0)))
            y = np.pad(y, ((0, padded_size - y.shape[0]), (0,0)))
            Xs.append(X)
            ys.append(y)
        X = np.stack(Xs)
        y = np.stack(ys)

    def mask_true_particles(self):
        pass