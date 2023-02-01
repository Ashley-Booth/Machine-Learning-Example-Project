'''
This file contains a dynamic basic model class that allows you to more easily tweak the parameters of a basic logistic regression model. 
'''
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from DataManager import DataManager
from matplotlib import pyplot as plt
import math
from keras.optimizers import SGD
class BasicModel:
    def __init__(self,path):
        self.DM = DataManager(path)
        self.train_values = pd.read_csv("./Data/training_data_with_vald.csv")["radius_mean"]
        self.train_diagnosis = pd.read_csv("./Data/training_data_with_vald.csv")["diagnosis_number"]
        self.vald_values = pd.read_csv("./Data/training_data_with_vald.csv")["radius_mean"]
        self.vald_diagnosis = pd.read_csv("./Data/training_data_with_vald.csv")["diagnosis_number"]

        self.test_values = pd.read_csv("./Data/testing_data_with_vald.csv")["radius_mean"]
        self.test_diagnosis = pd.read_csv("./Data/testing_data_with_vald.csv")["diagnosis_number"]
        #self.optimizer = SGD(lr=0.00001)
    def create_model(self):
        '''
        Create a basic machine learning model using the given parameters
        '''
        self.model = keras.Sequential(name="BasicModel")
        self.model.add(keras.layers.Dense(1,activation="selu",name="layerOne"))
        self.model.add(keras.layers.Dense(1,activation="sigmoid",name="layerTwo"))
        
        self.model.compile(optimizer ="Adam",loss="mse",metrics=["mae","mse"])
    def train_model(self,epochs=500):
        '''
        Train the model. 
        '''
        history = self.model.fit(self.train_values,self.train_diagnosis,epochs=epochs,validation_data=(self.vald_values,self.vald_diagnosis))
        plt.plot(history.history["mae"])
        plt.plot(history.history["val_mae"])
        plt.title("model mean absolute error")
        plt.xlabel("epoch")
        plt.ylabel("mean absolute error")
        plt.show()
        plt.plot(history.history["mse"])
        plt.plot(history.history["val_mse"])
        plt.title("model loss")
        plt.xlabel("epoch")
        plt.ylabel("loss")
        plt.show()
        # plt.plot(history.history["accuracy"])
        # plt.plot(history.history["val_accuracy"])
        # plt.title("model accuracy")
        # plt.xlabel("epoch")
        # plt.ylabel("accuracy")
        # plt.show()

    def train_and_validate_model(self):
        '''
        Train and validate a model
        '''
    def test_model(self):
        '''
        Test the model on testing data
        '''
        train_pred = self.model.predict(self.train_values)
        self.get_accuracy_metrics(train_pred,self.train_diagnosis)
        y_pred = self.model.predict(self.test_values)
        self.get_accuracy_metrics(y_pred,self.test_diagnosis)
        
    def get_accuracy_metrics(self,y_pred,true):
        '''
        Get a custom accuracy score and display a chi square analysis
        '''
        true_m = 0
        true_b = 0
        false_m = 0
        false_b = 0
        print(y_pred[0][0])
        
        pred=[]
        for i in range(len(y_pred)):
            if math.isclose(y_pred[i][0],true[i],rel_tol=0.15):
                if true[i]==0:
                    true_b+=1
                elif true[i]==1:
                    true_m+=1
            else:
                if round(y_pred[i][0])==0:
                    false_b+=1
                elif round(y_pred[i][0])==1:
                    false_m+=1
            pred.append(y_pred[i][0])
        print(true_m,true_b,false_m,false_b)
        print(f"Accuracy:{(true_m+true_b)/(true_b+true_m+false_m+false_b)}")
        plt.plot(range(len(pred)),pred)
        plt.show()

if __name__=="__main__":
    '''
    The following will only run if this is the function being run (not if imported into another function)
    '''
    model = BasicModel("./Data/data.csv")
    model.create_model()
    model.train_model()
    model.test_model()