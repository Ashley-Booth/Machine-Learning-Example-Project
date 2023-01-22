import pandas as pd
from matplotlib import pyplot as plt

class DataManager:
    def __init__(self,path,filter=True):
        '''
        This class will be how we interact and manage our dataset. 

        The initialization function includes a filter option as there is a lot of data in the dataset, some of which is more confusing than helpful. The built in filter function filters the dataset down 7 main columns. 
        '''
        self.data = pd.read_csv(path)
        if filter:
            self.filter()
        
    def filter(self):
        columns_keep = ["id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean"]
        for column in self.data.columns.values:
            if column not in columns_keep:
                self.data = self.data.drop(column,axis="columns")
        print(self.data.head())
    
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
        malignant = 0
        benign = 0
        for diagnosis in self.data["diagnosis"]:
            if diagnosis=="M": malignant+=1
            if diagnosis=="B": benign+=1
        if type.lower()=="bar":
            plt.bar("Maliganant",malignant,color="Red")
            plt.bar("Benign",benign,color="Green")
            plt.show()
        elif type.lower()=="pie":
            figure, ax1 = plt.subplots()
            ax1.pie([malignant,benign],labels=["malignant","benign"])
            ax1.axis('equal')
            plt.show()
        else:
            print("Please enter a valid type for visualize method")
    def summary(self):
        '''
        Displays the dataframe "head"
        '''
        print(self.data.head())
    def get_columns(self):
        '''
        Lists the database columns and the types that they each store. 
        '''
        columns = self.data.columns.values
        for column in columns:
            Type = type(self.data[column][0])
            print(f"{column}:   {Type}")
        

if __name__=="__main__":
    '''
    The following will only run if this is the file being run (it will not run if this file is imported into another)
    
    '''
    Dm = DataManager("./Data/data.csv")
    Dm.visualize(type="pie")
    #Dm.summary()
    #Dm.get_columns()

    