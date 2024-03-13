from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/")
def web_app():
    return render_template("index.html")

@app.route("/resume.html")
def web_app():
    return render_template("resume.html")


if __name__ == '__main__':
    app.run()