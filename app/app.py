from flask import Flask, request
from prometheus_client import start_http_server, Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Create Flask app & add prometheus wsgi middleware to route /metrics requests, see: https://github.com/prometheus/client_python#flask
app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Prometheus metrics
counter_requests = Counter('hello_worlds_total', 'Hello Worlds Requested.')
counter_exceptions = Counter('hello_world_exceptions_total', 'Exceptions serving Hello World.')

@app.route('/')
def hello_world():
    counter_requests.inc()  # Increment by 1
    return 'Hello, World!'

@app.route('/exception')
def raise_exception():
    counter_exceptions.inc()    # Increment by 1
    raise ZeroDivisionError

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
