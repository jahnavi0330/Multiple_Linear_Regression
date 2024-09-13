from hashlib import algorithms_available
import numpy as np
import pandas as pd
import sklearn
import sys
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,root_mean_squared_error

class TRAIN:
    def __init__(self,path):
        try:
            self.df = pd.read_csv(path,encoding = 'Latin-1')
            self.df = self.df.drop(['Customer Name','Customer e-mail','Country'],axis = 1)
            self.X = self.df.iloc[: ,:-1] #independent data
            self.y = self.df.iloc[: ,-1]  #dependent data
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=20)
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> {error_msg}')
    def train_data(self):
        try:
            self.reg=LinearRegression()
            self.reg.fit(self.X_train,self.y_train)  #training the algorithm
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> {error_msg}')

    def train_perfom(self):
        try:
            self.y_train_pred = self.reg.predict(self.X_train)
            print(f'training perfomance accuracy : {r2_score(self.y_train,self.y_train_pred)}')
            print(f'Loss by mean_squared_error : {mean_squared_error(self.y_train,self.y_train_pred)}')
            print(f'Loss by absolute_error : {mean_absolute_error(self.y_train,self.y_train_pred)}')
            print(f'Loss by absolute_error : {root_mean_squared_error(self.y_train,self.y_train_pred)}')
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> {error_msg}')

    def test_data(self):
        try:
            self.y_test_pred = self.reg.predict(self.X_test)
            print(f'testing perfomance accuracy : {r2_score(self.y_test, self.y_test_pred)}')
            print(f'Loss by mean_squared_error : {mean_squared_error(self.y_test, self.y_test_pred)}')
            print(f'Loss by absolute_error : {mean_absolute_error(self.y_test, self.y_test_pred)}')
            print(f'Loss by absolute_error : {root_mean_squared_error(self.y_test, self.y_test_pred)}')
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> {error_msg}')

if __name__ == "__main__":
    try:
        Tnobj = TRAIN('C:/Users/Lenovo/Downloads/ML/Multiple_Linear_Regression/Car_Purchasing_Data.csv')
        Tnobj.train_data()
        Tnobj.train_perfom()
        Tnobj.test_data()


    except Exception as e:
        error_type,error_msg,err_line = sys.exc_info()
        print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> {error_msg}')