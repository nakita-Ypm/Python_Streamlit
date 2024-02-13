import import_path as imp

imp.import_path("pages/file_edit")

from pages.file_edit import index as fe

FILE_EDIT = {
    "title": "XML Reader App",
    "api_endpoint": "http://flask:3001/parse_xml",
    "flie_type": "xml_file",
    "button": "Parse XML",
    "upload_title": "Upload XML",
    "type": "xml",
    "decode": "utf-8",
}

fe.apply(FILE_EDIT)
