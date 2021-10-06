from sanic.response import json
from sanic import Sanic

def ping(hostname:None):
    return {"data":"ola hostname"+hostname}

def report(data):
    return{"data":data}