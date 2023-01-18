# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:39:50 2023

@author: dell
"""
from functools import wraps
from flask import Flask, request, make_response, jsonify
import jwt
from data_analysis_storage import app

def Is_auth_route(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if auth and auth.username =="my user" and auth.password=="pass" :
            
            #generate the token
            token=jwt.encode({'user':auth.username}, app.config['SECRET_KEY'], algorithm="HS256")

            return f(*args,**kwargs)
        
        else:
            return make_response("Not authorized",401,{'WWW-Authenticate':'Basic realm= "login requierd"'})
        
    return decorated


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        token=request.args.get('token')
        if token==jwt.encode({'user':"my user"}, app.config['SECRET_KEY'], algorithm="HS256"):
            return f(*args,**kwargs)
        else:
            return jsonify({'message':'"You are not authorized to use this API!"'}),403
    return decorator 
