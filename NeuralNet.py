import tensorflow as tf
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.preprocessing import MinMaxScaler

neuralNet = Sequential([
    Dense(16, input_shape=(1,), activation='relu'), # This is the input layer
    Dense(32, activation='relu'),                   # This is the first hidden layer
    Dense(2, activation='softmax'),                    # This is the output layer
    ])

train_data = []
train_labels = []
test_data = []

scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_data = scaler.fit_transform((train_data).reshape(-1,1))


neuralNet.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

neuralNet.fit(scaled_train_data, train_labels, batch_size=10, epochs=20, shuffle=True, verbose=2)