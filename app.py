from flask import Flask, render_template, request
from model_plot import main
from predict_solubility import smiles_to_solubility
import numpy as np
import os


app = Flask(__name__) 



@app.route("/")
def web_app():
    return render_template("index.html")

@app.route("/resume.html")
def resume():
    return render_template("resume.html")

@app.route("/solubility", methods=['GET', 'POST'])
def sol_app():
    if request.method == "POST":
        smile_string = request.form.get("smiles")
        smile_sol = smiles_to_solubility([smile_string])
        return render_template("solubility.html", sol_val=list(smile_sol))
    return render_template("solubility.html")


if __name__ == '__main__':
    app.run()