from app import app
from flask import render_template, redirect, url_for, request
from app.forms import HatData
import random

@app.route("/", methods=["GET", "POST"])
def index():
    form = HatData()
    if form.validate_on_submit(): 
        return redirect("result")
    return render_template("index.html", form=form)

@app.route("/result", methods=["GET", "POST"])
def result():
    house = sortingThis()
    name = request.args.get('firstName')
    print(name)
    return render_template("result.html", house=house)

def sortingThis():
    l1 = ["Euro", "Orion", "Bubblegump", "Harazuh"]
    index = random.randint(0, 3)
    return l1[index]