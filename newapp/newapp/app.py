from newapp import get_model
from flask import Blueprint, render_template

from flask.ext.cors import CORS

appview = Blueprint('appview', __name__)
CORS(appview)

@appview.route("/")
def home():
    return render_template("home.html")

