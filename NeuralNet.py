from os.path import dirname
from os import listdir
import tensorflow as tf
import numpy as np
from random import randint
import keras
from keras import backend as K
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.preprocessing import MinMaxScaler
import csv
import itertools
import pandas as pd
from tsdbDataReader import *

# class DataObject:
#     def __init__(self, train_labels, train_samples, train_samples_row_1,train_samples_row_2,train_samples_row_3
#      , test_samples, test_samples_row_1, test_samples_row_2, test_samples_row_3, test_labels):
#         self.train_labels = []
#         self.train_samples = []
#         self.train_samples_row_1 = []
#         self.train_samples_row_2 = []
#         self.train_samples_row_3 = []
#         self.test_samples = []
#         self.test_samples_row_1 = []
#         self.test_samples_row_2 = []
#         self.test_samples_row_3 = []
#         self.test_labels = []


def getData():
    print("reading data")
    # print(len(readData()))
    iot_Data = readData()
    # def parseData():
    print(iot_Data[2])

    # shuffle data
    shuffledData = shuffleData(iot_Data)
    print(shuffledData[2])

    return shuffledData[:100000]

def prepareData(shuffledData):
    counter = 0
    train_labels = []
    train_samples_row_1 = []
    train_samples_row_2 = []
    train_samples_row_3 = []
    test_samples_row_1 = []
    test_samples_row_2 = []
    test_samples_row_3 = []
    test_labels = []
    for row in shuffledData:
        counter = counter + 1
        if(counter < 70001):
            train_samples_row_1.append(int(row[1]))
            train_samples_row_2.append(int(row[2]))
            train_samples_row_3.append(float(row[3]))
            train_labels.append(int(row[4]))
        else:
            test_samples_row_1.append(int(row[1]))
            test_samples_row_2.append(int(row[2]))
            test_samples_row_3.append(float(row[3]))
            test_labels.append(int(row[4]))

    train_samples_row_1 = np.array(train_samples_row_1)
    train_samples_row_2 = np.array(train_samples_row_2)
    train_samples_row_3 = np.array(train_samples_row_3)
    train_labels = np.array(train_labels)

    test_samples_row_1 = np.array(test_samples_row_1)
    test_samples_row_2 = np.array(test_samples_row_2)
    test_samples_row_3 = np.array(test_samples_row_3)
    test_labels = np.array(test_labels)

    return train_labels, test_labels, train_samples_row_1, train_samples_row_2, train_samples_row_3,test_samples_row_1,test_samples_row_2,test_samples_row_3

# data = getData()

# prepareData(data)

#for i in range(5000):
#    random_younger = randint(13,64)
#    train_samples.append(random_younger)
#    train_labels.append(0)

#    random_older = randint(65,100)
#    train_samples.append(random_older)
#    train_labels.append(1)

#for i in range(1000):
#    random_younger = randint(13,64)
#    train_samples.append(random_younger)
#    train_labels.append(1)

#    random_older = randint(65,100)
#    train_samples.append(random_older)
#    train_labels.append(0)



#for i in range(10):
#    random_younger = randint(13,64)
#    test_samples.append(random_younger)
#    test_labels.append(1)

#    random_older = randint(65,100)
#    test_samples.append(random_older)
#    test_labels.append(0)

#for i in range(200):
#    random_younger = randint(13,64)
#    test_samples.append(random_younger)
#    test_labels.append(0)

#    random_older = randint(65,100)
#    test_samples.append(random_older)
#    test_labels.append(1)

def transFormData():
    print("transforming data")
    scaler = MinMaxScaler(feature_range=(0,1))
    data = getData()

    train_labels, test_labels, train_samples_row_1, train_samples_row_2, train_samples_row_3,test_samples_row_1, test_samples_row_2,test_samples_row_3 = prepareData(data)
    scaled_train_sample_row_1 = scaler.fit_transform((train_samples_row_1).reshape(-1,1))
    scaled_train_sample_row_2 = scaler.fit_transform((train_samples_row_2).reshape(-1,1))
    scaled_train_sample_row_3 = scaler.fit_transform((train_samples_row_3).reshape(-1,1))
    scaled_test_sample_row_1 = scaler.fit_transform((test_samples_row_1).reshape(-1,1))
    scaled_test_sample_row_2 = scaler.fit_transform((test_samples_row_2).reshape(-1,1))
    scaled_test_sample_row_3 = scaler.fit_transform((test_samples_row_3).reshape(-1,1))

    for i in scaled_train_sample_row_1:
        train_samples = scaled_train_sample_row_1 + scaled_train_sample_row_2 + scaled_train_sample_row_3

    for i in scaled_test_sample_row_1:
        test_samples = scaled_test_sample_row_1 + scaled_test_sample_row_2 + scaled_test_sample_row_3

    return train_samples, test_samples, train_labels, test_labels

BATCH_SIZE = 1000
EPOCHS = 100

neuralNet = Sequential([
    Dense(3, input_shape=(1,), activation='relu'), # This is the input layer
    Dense(32, activation='relu'),                   # This is the first hidden layer
    Dense(3, activation='softmax'),                 # This is the output layer
    ])




neuralNet.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

train_samples, test_samples, train_labels, test_labels = transFormData()

#valid_set = [(sample, value),(sample, value),(sample, value),(sample, value)]
#validation_split = 0.1
print("Fitting frist time")
neuralNet.fit(train_samples, train_labels, batch_size=BATCH_SIZE, epochs=EPOCHS, shuffle=False, verbose=2)

predictions = neuralNet.predict(test_samples, batch_size=BATCH_SIZE, verbose=0)

rounded_prediction = neuralNet.predict_classes(test_samples, batch_size=BATCH_SIZE, verbose=0)

neuralNet.save("./saved_model.h5")



def predictionOutput(rounded_prediction, test_labels):
    correct = 0
    incorrect = 0
    for i in range(10000):
        # print("Prediction = " + str(rounded_prediction[i]) + " True Value = " + str(test_labels[i]))
        if(str(rounded_prediction[i]) == str(test_labels[i])):
            # print("correct")
            correct = correct + 1
        else:
            incorrect = incorrect + 1

    print("Correct", correct, "Incorrect", incorrect)

predictionOutput(rounded_prediction, test_labels)

def reTrainModel():
    train_samples, test_samples, train_labels, test_labels = transFormData()

    #valid_set = [(sample, value),(sample, value),(sample, value),(sample, value)]
    #validation_split = 0.1
    print("-----------------Fitting again-------------------")

    neuralNetR = load_model('./saved_model.h5')
    # neuralNet.load("./saved_model.h5")

    neuralNetR.fit(train_samples, train_labels, batch_size=BATCH_SIZE, epochs=EPOCHS, shuffle=False, verbose=2)

    predictions = neuralNetR.predict(test_samples, batch_size=BATCH_SIZE, verbose=0)

    rounded_prediction = neuralNetR.predict_classes(test_samples, batch_size=BATCH_SIZE, verbose=0)

    predictionOutput(rounded_prediction, test_labels)

    neuralNetR.save("./saved_model.h5")

for i in range(10):
    reTrainModel()