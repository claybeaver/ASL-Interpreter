from flask import Flask, render_template, Response
from Webcam_Recognition import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(show_webcam):
    while True:
        frame = show_webcam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)