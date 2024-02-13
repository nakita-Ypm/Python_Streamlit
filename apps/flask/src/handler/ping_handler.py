from flask import Flask, jsonify

def apply(app):
    @app.route("/", methods=["GET"])
    def hello():
        return "Hello World!"

    @app.route("/ping", methods=["GET"])
    def ping():
        data = {'message': 'pong'}
        return jsonify(data)