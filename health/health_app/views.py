from .main import app
from .constants import HOME_TEMPLATE, StatusCode
from flask import render_template


@app.route("/")
def home():
    try:
        return render_template(HOME_TEMPLATE, status_code=StatusCode.OK)
    except:
        return render_template(HOME_TEMPLATE, status_code=StatusCode.ERROR)
