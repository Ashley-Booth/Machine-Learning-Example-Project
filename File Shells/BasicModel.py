'''
This file is the shell for the BasicModel.py file, during the workshop we will walk through the steps of creating and training a logistic regression machine learning model and you can follow along and fill out this file as we go :)
'''

from DataManager import DataManager
class BasicModel:
    def __init__(self,path):
        self.DM = DataManager(path)
    
    def create_model(self):
        '''
        Create a basic machine learning model using the given parameters
        '''
    def train_model(self):
        '''
        Train the model. 
        '''
    def train_and_validate_model(self):
        '''
        Train and validate a model
        '''
    def test_model(self):
        '''
        Test the model on testing data
        '''
    def get_accuracy_metrics(self):
        '''
        Get a custom accuracy score and display a chi square analysis
        '''

if __name__=="__main__":
    '''
    The following will only run if this is the function being run (not if imported into another function)
    '''