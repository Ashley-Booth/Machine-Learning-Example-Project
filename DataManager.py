import pandas as pd
from matplotlib import pyplot as plt

class DataManager:
    def __init__(self,path):
        self.data = pd.read_csv(path)
    
    def print_data(self):
        '''
        Prints Data to terminal row by row (not recommended for large datasets)
        '''
        for i in self.data:
            print(self.data[i])
    
    def visualize(self, type="bar"):
        '''
        Displays the data as a given graph type. 
        Graph types include: bar, pie
        '''
        if type.lower()=="bar":
            print("foo")
        elif type.lower()=="pie":
            print("bar")
        else:
            print("Please enter a valid type for visualize method")
    def summary(self):
        '''
        Displays the dataframe "head"
        '''
    def get_columns(self):
        '''
        Lists the database columns and the types that they each store. 
        '''

if __name__=="__main__":
    '''
    The following will only run if this is the file being run (it will not run if this file is imported into another)
    '''
    Dm = DataManager("Data/data.csv")