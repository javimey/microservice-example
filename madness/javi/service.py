# -*- coding: utf-8 -*-
import uwsgi
import falcon
import ujson
import logging
from madness.javi.client import Client

class Service():
    def __init__(self):
        self.client = Client()

    def on_get(self, req, resp):
        data = self.client.set_get(data=req.params)
        response_body = self.client.exec_get(data=data)
        resp.body = ujson.dumps(response_body)

class ServicePing():
    def __init__(self):
      pass

    def on_get(self, req, resp):
        pass

# falcon.API instances are callable WSGI apps
app = falcon.API()
app.add_route('/doychin', Service())
app.add_route('/ping', ServicePing())
