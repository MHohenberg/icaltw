#!/usr/bin/python3

import socketserver
import os
from config_handler import ConfigHandler
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class CalDAVServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

config = ConfigHandler('./twconfig').read()

PORT = int(config['SERVER']['port'])
ssl_keyfile=config['SERVER']['ssl_keyfile']
ssl_certfile=config['SERVER']['ssl_certfile']

httpd = HTTPServer(('localhost', PORT), CalDAVServerRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile=ssl_keyfile, 
        certfile=ssl_certfile, server_side=True)

httpd.serve_forever()
