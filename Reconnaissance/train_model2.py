import tensorflow as tf
import cv2
from grid_extractor import *
from tensorflow.examples.tutorials.mnist import input_data

img = cv2.imread('exemple 1.jpg', cv2.IMREAD_COLOR)

digit = parse_grid("exemple 1.jpg")

import pickle

pickle_in = open("digit-basic","rb")
dataset = pickle.load(pickle_in)


(x_train, y_train), (x_test, y_test) = (dataset.train.images,dataset.train.labels) ,(dataset.test.images,dataset.train.labels)
x_train, x_test = x_train / 255.0, x_test / 255.0

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

    model.evaluate(x_test,  y_test, verbose=2)

train()


model.save('model.h5')
#model = train(digit[0].reshape(1,28,28))


