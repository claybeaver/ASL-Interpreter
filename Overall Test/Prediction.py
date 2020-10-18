import base64
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model




def predict(base64string):
    imgdata = base64.b64decode(base64string)
    filename = 'prediction_image.jpg'
    with open(filename, 'wb') as f:
        image = f.write(imgdata)

    img = image.load_img(image, target_size = (100,100,3), color_mode = "rgb")
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
    X = np.array(train_image)

    model = load_model('model_1.h5', compile = True)

    encoded_predictions = model.predict_classes(X[:])
    prediction_labels = label_encoder.inverse_transform(encoded_predictions)

