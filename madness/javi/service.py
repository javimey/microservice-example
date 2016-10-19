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

    # def on_post(self, req, resp):
    #     user = self.client.set_post(data=ujson.loads(req.stream.read()))
    #     response_body = self.client.exec_post(user=user)
    #     resp.body = ujson.dumps(response_body)
    #

# falcon.API instances are callable WSGI apps
app = falcon.API()
app.add_route('/', Service())
