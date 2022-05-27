
import bz2, pickle
import matplotlib as plt

class DataLoader():

    def __init__(self):
        pass

class EventLoader(DataLoader):

    def __init__(self, filename):
        self.data = pickle.load(bz2.BZ2File(filename, "r"))