# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:39:50 2023

@author: dell
"""
from functools import wraps
from flask import Flask, request, make_response, jsonify


def Is_auth_route(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if auth and auth.username =="my user2" and auth.password=="pass" :
            #generate the token
            #token=jwt.encode({'user':auth.username})
            return f(*args,**kwargs)
        
        else:
            return make_response("Not authorized",401,{'WWW-Authenticate':'Basic realm= "login requierd"'})
        
    return decorated


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        token=request.args.get('token')
        if token==True:
            return jsonify({'token': token.decode('UTF-8')})
