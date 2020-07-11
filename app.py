from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__, template_folder='templates')

cities = ["Raipur",
          "Ranchi",
          "Rajkot",
          "Ludhiana",
          "Agra",
          "Agartala",
		  "Bangalore",
          "Vellore",
          "Nellore",
          "Warrangal",
		  "Kolkata",
		  "Kozhikode"]


class SearchForm(Form):
    autocomp = TextField('Insert City', id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(cities), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)