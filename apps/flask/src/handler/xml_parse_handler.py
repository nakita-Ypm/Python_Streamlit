from flask import Flask, request, jsonify

def apply(app):
    @app.route("/parse_xml", methods=["POST"])
    def parse_xml():
        # POSTリクエストからXMLファイルを取得
        xml_file = request.files.get("xml_file")

        if xml_file is None:
            return "XMLファイルが提供されていません。", 400

        try:
            xml_content = xml_file.read()
            print(xml_content)
            return xml_content, 200
        except Exception as e:
            return f"XMLデータの処理中にエラーが発生しました: {str(e)}", 500




    # @app.route("/ping", methods=["GET"])
    # def ping():
    #     data = {'message': 'pong'}
    #     return jsonify(data)