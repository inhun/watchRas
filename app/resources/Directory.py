from flask_restful import Resource, reqparse, request
from app.models.response import error_response, ok_response
from flask import current_app as app
from flask import jsonify, make_response
import os
import json
import unicodedata


class GETDir(Resource):
    def get(self, content):
        files = []
        directory = []

        try:
            filenames = os.listdir(f'/home/pi/ShareDir/{content}')
            for filename in filenames:
                if os.path.isfile(f'/home/pi/ShareDir/{content}/{filename}'):
                    files.append(filename)
                else:
                    directory.append(filename)

        except Exception as exc:
            return error_response(500, f'{exc}')
            
        
        return ok_response({
            'files': files,
            'directory': directory
        })


class GETRoot(Resource):
    def get(self):
        files = []
        directory = []
        try:
            filenames = os.listdir('/home/pi/ShareDir')
            for filename in filenames:
                if os.path.isfile(f'/home/pi/ShareDir/{filename}'):
                    files.append(filename)
                else:
                    directory.append(filename)

        except Exception as exc:
            return error_response(500, f'{exc}')


        return ok_response({
            'files': files,
            'directory': directory
        })

