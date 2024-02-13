import requests


def post_file(api_endpoint, file_type, uploaded_file):
    return requests.post(api_endpoint, files={file_type: uploaded_file})
