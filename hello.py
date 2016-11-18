def app(environ, start_response):
 # logic
 status = '200 OK'
 headers = [
  ('Content-Type', 'text/plain')
  ]
 body = environ['QUERY_STRING'].split("&")
 body = [i+'\r\n' for i in body]
 start_response(status, headers )
 return body

 # gunicorn config
CONFIG = {
  'working_dir': '/home/box/web/etc/hello.py',
  'args': (
   'bind = "0.0.0.0:8080"'
   ),
 }