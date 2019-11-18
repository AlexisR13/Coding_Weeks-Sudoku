import pickle
import cv2
import numpy as np

pickle_in = open("digit-basic","rb")
dataset = pickle.load(pickle_in)

(x_train, y_train), (x_test, y_test) = (dataset.train.images,dataset.train.labels) ,(dataset.test.images,dataset.train.labels)
x,y = dataset.train.next_batch(2)

print(np.shape(x[0]))

"""
cv2.imshow('image', x[0].reshape())  # Show the image
cv2.waitKey(0)  # Wait for any key to be pressed (with the image window active)
cv2.destroyAllWindows()  # Close all windows
"""