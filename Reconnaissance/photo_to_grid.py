import tensorflow as tf
import cv2
from Reconnaissance.transform_photo_grid import *

def analyse(array):
    for i in range(len(array)):
        if array[i] > 0.9:
            return i





def photo_to_grid(path):
    model = tf.keras.models.load_model('Reconnaissance/mnistCNN.h5')
    digit = parse_grid(path)
    grid = np.full((9,9), "")
    pure_black(digit)
    pure_white(digit)

    for i in range(len(digit)):
        if is_empty(digit[i]):
            grid[i//9][i%9] = ""
        else:
            arr = (model.predict(np.float64(digit[i].reshape(1,28,28,1))))
            arr = analyse(arr[0])
            
            grid[i//9][i%9] =  str(arr)

    return grid
