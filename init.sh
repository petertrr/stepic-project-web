ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

gunicron -c /home/box/web/etc/hello.py hello:app --daemon
gunicron -c /home/box/web/ask/qa/views.py views:test --daemon