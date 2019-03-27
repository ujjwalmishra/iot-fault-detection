from influxdb import InfluxDBClient
import tensorflow as tf
import numpy as np
import keras
from keras import backend as K
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from tsdbDataReader import *
from writeResultTsdb import *

client = InfluxDBClient(host='localhost', port=8086)

client.switch_database('pyexample')

#The specifics of the query need to be set for our database
results = client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')

points = results.get_points(tags={'Key':'Value'})

data = []
values = []
# The points need to be seperated into data and values

BATCH_SIZE = 1000
EPOCHS = 100

neuralNet = Sequential([
    Dense(3, input_shape=(1,), activation='relu'), # This is the input layer
    Dense(32, activation='relu'),                   # This is the first hidden layer
    Dense(3, activation='softmax'),                 # This is the output layer
    ])

neuralNet.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

neuralNet.fit(data, values, batch_size=BATCH_SIZE, epochs=EPOCHS, shuffle=False, verbose=2)
