import tensorflow as tf
import cv2
from grid_extractor import *


def convert(ligne):
    ligne = np.array(ligne)
    grid = np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            grid[i][j] = ligne[i*28+j]
    return grid


import pickle

pickle_in = open("digit-basic","rb")
dataset = pickle.load(pickle_in)


def index_max(ligne):
    i = 0
    for k in range(len(ligne)):
        if ligne[k] > ligne[i]:
            i = k
    return i

(x_train, y_train), (x_test, y_test) = (dataset.train.images,dataset.train.labels) ,(dataset.test.images,dataset.train.labels)
x_train, x_test = x_train, x_test

x_train = np.array([ convert(x) for x in x_train])
y_train = np.array([index_max(x) for x in y_train])
x_test = np.array([ convert(x) for x in x_test])
y_test = np.array([index_max(x) for x in y_test])

model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

def train():
    model.fit(x_train, y_train, epochs=5)

    #model.evaluate(x_test,  y_test, verbose=2)

train()


model.save('model2.h5')


