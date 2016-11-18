def app(environ, start_response):
 # logic
 status = '200 OK'
 headers = [
  ('Content-Type', 'text/plain')
  ]
 body = environ['QUERY_STRING'].split("&")
 start_response(status, headers )
 return iter([ body ])

 # gunicorn config
CONFIG = {
  'working_dir': '/home/box/web/etc/hello.py',
  'args': (
   'bind = "0.0.0.0:8080"'
   ),
 }