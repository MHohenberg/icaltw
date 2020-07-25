#!/usr/bin/python3

import http.server
import socketserver
import os
from config_handler import ConfigHandler

config = ConfigHandler('./twconfig').read()

PORT = int(config['SERVER']['port'])
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
