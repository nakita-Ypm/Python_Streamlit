from flask import Flask, jsonify

def apply(app):
    @app.route("/fcp", methods=["GET"])
    def parse():
        return "fcp"

    # @app.route("/ping", methods=["GET"])
    # def ping():
    #     data = {'message': 'pong'}
    #     return jsonify(data)