import os
import json
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask import Flask,request,render_template,session,jsonify,make_response

app=Flask(__name__)

engine=create_engine("postgres://znxhdlasrqzttu:ba5642dacee20976d5f9d521d35dd743fb59ba76cdd6c1f748a578729f788d5c@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d5as70ja4tlr")
db=scoped_session(sessionmaker(bind=engine))

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/")
def index():
    return """Hello world!"""

@app.route("/api/<string:enroll>",methods=["GET"])
def api(enroll):
    # books=db.execute("select isbn from books where isbn=:isbn",{"isbn":isbn})
    try:
        item=db.execute("select enroll,fname,lname,email,dept,grad_year from college where enroll=:enroll",{"enroll":enroll}).fetchone()
        print("a")
        result=dict(item.items())
        print(result)
        print("b")
        print(result)
        x = make_response(jsonify(result))
        print("c")
        return x
    except:
        return "404: enroll does not found"
