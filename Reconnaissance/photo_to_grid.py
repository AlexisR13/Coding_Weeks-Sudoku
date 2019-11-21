import tensorflow as tf
import cv2
from Reconnaissance.transform_photo_grid import *

def analyse(array):
    for i in range(len(array)):
        if array[i] > 0.9:
            return i


def photo_to_grid(path,model):
    
    digit = parse_grid(path)
    
    
    if model == 'ordi':    
        model = tf.keras.models.load_model('Reconnaissance/model.h5')
        digit_reshape  = np.float64(np.array([x.reshape(1,28,28) for x in digit]))  
        print("11111111")

    else:
        model = tf.keras.models.load_model('Reconnaissance/mnistCNN.h5')
        digit_reshape  = np.float64(np.array([x.reshape(1,28,28,1) for x in digit]))
        print("2222222222")
    
    grid = np.full((9,9), "")
    pure_black(digit)
    pure_white(digit)

    for i in range(len(digit)):
        if is_empty(digit[i]):
            grid[i//9][i%9] = ""
        else:
            arr = (model.predict(digit_reshape[i]))
            arr = analyse(arr[0])
            if arr == 0:
                arr =1
            grid[i//9][i%9] =  str(arr)

    return grid
