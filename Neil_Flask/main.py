
from flask import Flask, render_template, Response, request
from Webcam_Recognition import VideoCamera
import cv2

app = Flask(__name__)

@app.route('/')
def camera():
    return render_template('index.html')


@app.route('/image', methods=['GET','POST'])
def signup():
    print('Test')
    if request.method == 'POST':
        return jsonify(request.form['userID'], request.form['file'])
    return render_template('image.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
