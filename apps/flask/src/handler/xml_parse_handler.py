from flask import Flask, request, jsonify

import import_path as imp

imp.import_path("domain")
imp.import_path("service")

from domain import xml_parse_domain as xp
from service import google_translate_service as gt

def apply(app):
    @app.route("/parse_xml", methods=["POST"])
    def parse_xml():
        xml_file = request.files.get("xml_file")

        if not xml_file:
            return "XMLファイルが提供されていません。", 400

        try:
            res = ""

            xml_content = xml_file.read()

            lxml = xp.lxml(xml_content)

            count = 0

            for l in lxml:
                parent = l.getparent()
                parent_offset, parent_start = xp.get_parent_info(parent)

                offset, duration = map(l.get, ['offset', 'duration'])

                start, end = xp.calculate_time(parent_offset, offset, parent_start, duration)

                start_time = xp.to_hms_ms(start)
                end_time = xp.to_hms_ms(end)

                text_styles = l.xpath('.//text-style')
                text_style = xp.get_text_style(text_styles)

                if text_style != "None":
                    count = count + 1
                    res += xp.cerate_srt(count, start_time, end_time, gt.google_translation(text_style))
            
            return res, 200
        except Exception as e:
            return f"XMLデータの処理中にエラーが発生しました: {e}", 500