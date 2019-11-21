import tensorflow as tf
import cv2
from Reconnaissance.Reconnaissance_image import *
import operator

def analyse(array):
    return max(enumerate([i for i in array]), key=operator.itemgetter(1))[0]



def photo_to_grid(path,model):
    
    digit = grille_extraite(path)
    
    
    if model == 'ordi':    
        model = tf.keras.models.load_model('Reconnaissance/model2.h5')
        digit_reshape  = np.float64(np.array([x.reshape(1,28,28) for x in digit]))  
    else:
        model = tf.keras.models.load_model('Reconnaissance/mnistCNN.h5')
        digit_reshape  = np.float64(np.array([x.reshape(1,28,28,1) for x in digit]))
    
    grid = np.full((9,9), "")


    for i in range(len(digit)):
        if is_empty(digit[i]):
            grid[i//9][i%9] = ""
        else:
            arr = (model.predict(digit_reshape[i]))
            print(arr)
            arr = analyse(arr[0])
            if arr == 0:
                arr =1
            print(arr)
            grid[i//9][i%9] =  str(arr)
    print(grid)
    return grid
