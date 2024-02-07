from flask import Flask, request, jsonify

import import_path as imp

imp.import_path("domain")

from domain import xml_parse_domain as xp

def apply(app):
    @app.route("/parse_xml", methods=["POST"])
    def parse_xml():
        # POSTリクエストからXMLファイルを取得
        xml_file = request.files.get("xml_file")

        if not xml_file:
            return "XMLファイルが提供されていません。", 400

        try:
            xml_content = xml_file.read()
            res = xp.tree(xml_content)
            return res, 200
        except Exception as e:
            return f"XMLデータの処理中にエラーが発生しました: {e}", 500




    # @app.route("/ping", methods=["GET"])
    # def ping():
    #     data = {'message': 'pong'}
    #     return jsonify(data)