#coding=utf-8

try:
    import matplotlib.pyplot as plt
except:
    pass

try:
    import pandas as pd
except:
    pass

try:
    from sklearn.model_selection import train_test_split
except:
    pass

try:
    from tensorflow.keras.models import Sequential
except:
    pass

try:
    from tensorflow.keras.layers import Conv2D
except:
    pass

try:
    from tensorflow.keras.layers import MaxPooling2D
except:
    pass

try:
    from tensorflow.keras.layers import Flatten
except:
    pass

try:
    from tensorflow.keras.layers import Dense
except:
    pass

try:
    from tensorflow.keras.layers import Dropout
except:
    pass

try:
    from tensorflow.keras.preprocessing import image
except:
    pass

try:
    from tensorflow.keras.utils import to_categorical
except:
    pass

try:
    from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
except:
    pass

try:
    from sklearn.preprocessing import LabelEncoder
except:
    pass

try:
    from tqdm import tqdm
except:
    pass

try:
    import numpy as np
except:
    pass
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

X_train2, X_val, y_train2, y_val = train_test_split(X_train, y_train_cat, random_state=42, test_size=0.2)

  x_train = X_train
  y_train = y_train_cat
  x_test = X_test
  y_test = y_test_cat


def keras_fmin_fnct(space):

    model = Sequential()
    model.add(Conv2D(space['Conv2D'], kernel_size=space['kernel_size'],padding="valid",activation='relu',input_shape=(28, 28, 3)))
    model.add(Conv2D(space['Conv2D_1'], kernel_size=space['kernel_size_1'],padding="valid", activation='relu'))
    model.add(MaxPooling2D(pool_size=space['pool_size']))
    model.add(Dropout(space['Dropout']))
    model.add(Flatten())
    #model.add(Dense(64, activation='relu'))
    model.add(Dense(space['Dense']))
    model.add(Activation(space['Activation']))
    model.add(Dropout(space['Dropout_1']))
    #model.add(Dropout(0.5))
    model.add(Dense(26, activation='softmax'))    
    # Compile Model
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    
    # Fit Model
    model.fit(x_train, y_train, epochs=space['epochs'],verbose=10, validation_data=(X_test, y_test))
    
    return model

def get_space():
    return {
        'Conv2D': hp.choice('Conv2D', [26, 52, 104]),
        'kernel_size': hp.choice('kernel_size', [(3, 3),(5,5)]),
        'Conv2D_1': hp.choice('Conv2D_1', [26, 52, 104]),
        'kernel_size_1': hp.choice('kernel_size_1', [(3, 3),(5,5)]),
        'pool_size': hp.choice('pool_size', [(2, 2),(4,4)]),
        'Dropout': hp.uniform('Dropout', 0, 1),
        'Dense': hp.choice('Dense', [256, 512, 1024]),
        'Activation': hp.choice('Activation', ['relu', 'tanh']),
        'Dropout_1': hp.uniform('Dropout_1', 0, 1),
        'epochs': hp.choice('epochs', [20,50,100]),
    }
