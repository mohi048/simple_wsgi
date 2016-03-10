## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script for a simple wsgi
## usage python mysimplewsgi.py 9000 
## This would listen on port 9000 , to access page point to http://server-ip:9000

import sys
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']


httpd = make_server('', int(sys.argv[1]), simple_app)
print "Serving HTTP on port {0}...".format(sys.argv[1])

  # Respond to requests until process is killed
httpd.serve_forever()

 # Alternative: serve one request, then exit
 ##httpd.handle_request()