import import_path as imp

imp.import_path("pages/file_edit")

from pages.file_edit import index as fe

FILE_EDIT = {
    "title": "XML Reader App",
    "api_endpoint": "http://flask:3001/parse_xml",
    "upload_title": "Upload XML",
    "flie_format": "xml_file",
    "type": "xml",
    "button": "Parse XML",
}

fe.apply(FILE_EDIT)
