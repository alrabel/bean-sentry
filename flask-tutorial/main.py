#import Flask module and create a Flask web server
from flask import Flask, Response, render_template

#emulated test camera
from camera import Camera

#TODO: raspi camera
#from camera_pi import Camera

#new instance of Flask class called app
#current file represents the web app
app = Flask(__name__)

#default page route loads the home HTML template
@app.route("/")
def home():
    #homepage
    return render_template("home.html")
    
def gen(camera):
    #video streaming generator function
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#route to a different page
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#python assigns the name __main__ to the script when exec
#this statement prevents other scripts from running
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)

#test out by going to localhost:5000 in browser
