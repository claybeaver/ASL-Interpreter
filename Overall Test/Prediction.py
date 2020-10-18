import base64
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from sklearn.preprocessing import LabelEncoder

import io
import PIL


def predict(base64string):
    train_image = []
    imgdata = base64.b64decode(base64string)
    img = PIL.Image.open(io.BytesIO(imgdata))
    # img = image.load_img(img, target_size = (100,100,3), color_mode = "rgb")
    img = img.resize((100, 100)).convert(mode="L")
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
    X = np.array(train_image)

    model = load_model('model_1.h5', compile = True)

    images_names = pd.read_csv('../Image Values2.csv')
    labels = images_names['Image Value'].values
    label_encoder = LabelEncoder()
    label_encoder.fit(labels)

    encoded_predictions = model.predict_classes(X[:])
    prediction_labels = label_encoder.inverse_transform(encoded_predictions)
    print('######## PREDICTION #########')
    print(prediction_labels)
    print('######## PREDICTION #########')
    return prediction_labels[0]

