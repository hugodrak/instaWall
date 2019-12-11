from flask import Flask, render_template
import os
app = Flask(__name__)

imgdir = "static/dl"

@app.route('/')
def main():
    dirs = [x[1] for x in os.walk(imgdir)][0]
    data = []
    for d in dirs:
        pics = []
        for pic in os.listdir(imgdir+"/"+d):
            pics.append("./"+imgdir+"/"+d+"/"+pic)
        data.append([d, pics])
    return render_template("main.html", data=data)


if __name__ == '__main__':
    app.run()
