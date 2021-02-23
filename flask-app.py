#!/usr/bin/env python
# (C) 2020-2021 Keir Finlow-Bates
# See LICENSE for the licensing details of this software

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'mysecretkey'

# Route for serving up the index page
@app.route('/')
def index():
    return "<h1>Flask</h1><p>Flask is running.</p>", 200 
