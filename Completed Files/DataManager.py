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
        #print(self.data.head())
    
    def print_data(self):
        '''
        Prints Data to terminal row by row (not recommended for large datasets)
        '''
        for i in self.data:
            print(self.data[i])
    
    def visualize_distribution(self, type="bar"):
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
    
    def visualize_specific(self, column="texture_mean"):
        '''
        Graphs a given radius_mean column against the diagnosis_number column
        '''
        plt.scatter(self.data[column],self.data["diagnosis_number"])
        plt.xlabel(column)
        plt.ylabel("Diagnosis")
        plt.title(f"{column} and Diagnosis ")
        plt.show()

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
    
    def featurize_data(self):
        '''
        Featurizes the diagnosis data into a model readable format.
        '''
        self.data["diagnosis_number"]=0
        for i in range(len(self.data)):
            if self.data["diagnosis"][i] == "M":
                self.data["diagnosis_number"][i] = 1
            elif self.data["diagnosis"][i]=="B":
                self.data["diagnosis_number"][i] = 0
        print(self.data.head())
    #Model helper Functions:
    def train_test_split(self,path="./Data"):
        '''
        Split the data into training and test datasets
        '''
        self.data=self.data.sample(frac=1)

        training_data = self.data[:round((len(self.data)*.9))]
        testing_data = self.data[round((len(self.data)*.9)):]

        train = pd.DataFrame(training_data)
        test = pd.DataFrame(testing_data)

        train.to_csv(f"{path}/training_data.csv")
        test.to_csv(f"{path}/testing_data.csv")
        print(f'Training and testing datasets created and saved to {path}')
        
    def train_valid_train_split(self):
        '''
        Split the data into training, validation, and test datasets
        '''
    
        

if __name__=="__main__":
    '''
    The following will only run if this is the file being run (it will not run if this file is imported into another)
    
    '''
    Dm = DataManager("./Data/data.csv")
    Dm.featurize_data()

    #Dm.visualize(type="pie")
    #Dm.summary()
    #Dm.get_columns()

    