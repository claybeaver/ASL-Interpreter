from flask import Flask, render_template, Response
from Webcam_Recognition import show_webcam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(show_webcam):
    while True:
        frame = show_webcam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(show_webcam()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='5000', debug=True)