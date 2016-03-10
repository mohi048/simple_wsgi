## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script for a simple wsgi
## usage python classwaywsgi.py 9000
## This would listen on port 9000 , to access page point to http://server-ip:9000

class SimpleApp:
      def __init__(self, environ, start_response):
          self.environ = environ
          self.start = start_response

      def __iter__(self):
          status = '200 OK'
          response_headers = [('Content-type','text/plain')]
          self.start(status, response_headers)
          yield 'My class way Hello world!\n'

from wsgiref.simple_server import make_server
import sys

httpd = make_server('', int(sys.argv[1]), SimpleApp)
print "Serving HTTP on port {0}...".format(sys.argv[1])

# Respond to requests until process is killed
httpd.serve_forever()
