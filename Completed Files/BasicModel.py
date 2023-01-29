'''
This file contains a dynamic basic model class that allows you to more easily tweak the parameters of a basic logistic regression model. 
'''
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from DataManager import DataManager
from matplotlib import pyplot as plt
from keras.optimizers import SGD
class BasicModel:
    def __init__(self,path):
        self.DM = DataManager(path)
        self.train_values = pd.read_csv("./Data/training_data.csv")[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean"]]
        self.train_diagnosis = pd.read_csv("./Data/training_data.csv")["diagnosis_number"]
        self.test_values = pd.read_csv("./Data/testing_data.csv")[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean"]]
        self.test_diagnosis = pd.read_csv("./Data/testing_data.csv")["diagnosis_number"]
        
        self.input_shape = self.train_values.shape[1:]
        #self.output_shape = self.train_diagnosis.shape[1]
        self.optimizer = SGD(lr=0.000001)

    def create_model(self):
        '''
        Create a basic machine learning model using the given parameters
        '''
        self.model = keras.Sequential(name="BasicModel")
        self.model.add(keras.layers.Dense(5,activation="relu",name="layerOne",input_shape=self.input_shape))
        self.model.add(keras.layers.Dense(1,activation="relu",name="layerTwo"))
        
        self.model.compile(optimizer ="Adam",loss="mean_squared_error",metrics=["mae","mse"])
    def train_model(self,epochs=50):
        '''
        Train the model. 
        '''
        history = self.model.fit(self.train_values,self.train_diagnosis,epochs=epochs)
        plt.plot(history.history["mae"])
        plt.title("model accuracy")
        plt.xlabel("epoch")
        plt.ylabel("accuracy")
        plt.show()

    def train_and_validate_model(self):
        '''
        Train and validate a model
        '''
    def test_model(self):
        '''
        Test the model on testing data
        '''
        y_pred = self.model.predict(self.test_values)
        print(y_pred[0])
        self.get_accuracy_metrics(y_pred)
        
    def get_accuracy_metrics(self,y_pred):
        '''
        Get a custom accuracy score and display a chi square analysis
        '''
        true_m = 0
        true_b = 0
        false_m = 0
        false_b = 0
        for i in range(len(y_pred)):
            if int(y_pred[i]) == self.test_diagnosis[i]:
                if self.test_diagnosis[i]==0:
                    true_b+=1
                if self.test_diagnosis[i]==1:
                    true_m+=1
            else:
                if int(y_pred[i])==0:
                    false_b+=1
                if int(y_pred[i])==1:
                    false_m+=1
        print(true_m,true_b,false_m,false_b)

if __name__=="__main__":
    '''
    The following will only run if this is the function being run (not if imported into another function)
    '''
    model = BasicModel("./Data/data.csv")
    model.create_model()
    model.train_model()
    model.test_model()