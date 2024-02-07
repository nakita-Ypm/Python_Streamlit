import xml.etree.ElementTree as ET

def tree(xml_content):
    try:
        tree = ET.fromstring(xml_content)
        print(tree)
        root = tree.getroot()
        print(root)
        res = ET.tostring(root, encoding="utf-8", method="xml")
        print(res)
        return res
        
    except Exception as e:
        return f"XMLデータの処理中にエラーが発生しました: {e}"