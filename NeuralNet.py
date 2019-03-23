from os.path import dirname
from os import listdir
import tensorflow as tf
import numpy as np
from random import randint
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.preprocessing import MinMaxScaler
import csv
import itertools
import pandas as pd

train_labels = []
train_samples = []
train_samples_row_1 = []
train_samples_row_2 = []
train_samples_row_3 = []
test_samples = []
test_samples_row_1 = []
test_samples_row_2 = []
test_samples_row_3 = []
test_labels = []

counter = 0

with open('BaseLine-Faulty-merged.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        counter = counter + 1
        if(counter < 100000):
            train_samples_row_1.append(row[0])
            train_samples_row_2.append(row[1])
            train_samples_row_3.append(row[2])
            train_labels.append(row[4])
        else:
            test_samples_row_1.append(row[0])
            test_samples_row_2.append(row[1])
            test_samples_row_3.append(row[2])
            test_labels.append(row[4])

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

train_samples_row_1 = np.array(train_samples_row_1)
train_samples_row_2 = np.array(train_samples_row_2)
train_samples_row_3 = np.array(train_samples_row_3)
train_labels = np.array(train_labels)

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

test_samples_row_1 = np.array(test_samples_row_1)
test_samples_row_2 = np.array(test_samples_row_2)
test_samples_row_3 = np.array(test_samples_row_3)
test_labels = np.array(test_labels)



BATCH_SIZE = 500
EPOCHS = 100

neuralNet = Sequential([
    Dense(16, input_shape=(1,), activation='relu'), # This is the input layer
    Dense(32, activation='relu'),                   # This is the first hidden layer
    Dense(3, activation='softmax'),                 # This is the output layer
    ])


scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_sample_row_1 = scaler.fit_transform((train_samples_row_1).reshape(-1,1))
scaled_train_sample_row_2 = scaler.fit_transform((train_samples_row_2).reshape(-1,1))
scaled_train_sample_row_3 = scaler.fit_transform((train_samples_row_3).reshape(-1,1))
scaled_test_sample_row_1 = scaler.fit_transform((test_samples_row_1).reshape(-1,1))
scaled_test_sample_row_2 = scaler.fit_transform((test_samples_row_2).reshape(-1,1))
scaled_test_sample_row_3 = scaler.fit_transform((test_samples_row_3).reshape(-1,1))

neuralNet.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

for i in scaled_train_sample_row_1:
    train_samples = scaled_train_sample_row_1 + scaled_train_sample_row_2 + scaled_train_sample_row_3

for i in scaled_test_sample_row_1:
    test_samples = scaled_test_sample_row_1 + scaled_test_sample_row_2 + scaled_test_sample_row_3


#valid_set = [(sample, value),(sample, value),(sample, value),(sample, value)]
#validation_split = 0.1
neuralNet.fit(train_samples, train_labels, batch_size=BATCH_SIZE, epochs=EPOCHS, shuffle=False, verbose=2)

predictions = neuralNet.predict(test_samples, batch_size=BATCH_SIZE, verbose=0)

rounded_prediction = neuralNet.predict_classes(test_samples, batch_size=BATCH_SIZE, verbose=0)

correct = 0
incorrect = 0

for i in range(10000):
    print("Prediction = " + str(rounded_prediction[i]) + " True Value = " + str(test_labels[i]))
    if(str(rounded_prediction[i]) == str(test_labels[i])):
        print("correct")
        correct = correct + 1
    else:
        print("incorrect")
        incorrect = incorrect + 1

print("Correct", correct, "Incorrect", incorrect)
