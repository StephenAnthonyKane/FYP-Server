#!C:/Users/steve/AppData/Local/Programs/Python/Python37-32/python
from PostHandler import PostHandler
from GetHandler import GetHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import socketserver

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        getHandler = GetHandler()

        urlParams = urlparse(self.path).query
        values = getHandler.Handle(urlParams)

        print(values)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile=values

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers()
        print("Post request recived")
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        postHandler = PostHandler()
        postHandler.Handle(post_data)
        
httpd = socketserver.TCPServer(("192.168.1.21", 8080), MyHandler)
httpd.serve_forever()