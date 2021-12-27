# Import Dependencies
from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import re
from sqlalchemy import create_engine
import psycopg2
#from config import db_password
import time
import model

# Start Setup
app=Flask(__name__)

#default page of our web-app
@app.route('/', methods=['GET', 'POST'])

def index():
    averageBill=""
    errors=[]
    panelsNeeded=[]

    if request.methon=="Get":
        from model import Data['number_of_panels']
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)