import tensorflow as tf
import cv2
from grid_extractor import *

model = tf.keras.models.load_model('model.h5')

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

img = cv2.imread('exemple 1.jpg', cv2.IMREAD_COLOR)

digit = parse_grid("exemple 1.jpg")

arr = (model.predict(x_test[0].reshape(1,28,28)))
print(np.where(arr == np.amax(arr)))


cv2.imshow('image', x_test[0])  # Show the image
cv2.waitKey(0)  # Wait for any key to be pressed (with the image window active)
cv2.destroyAllWindows()  # Close all windows