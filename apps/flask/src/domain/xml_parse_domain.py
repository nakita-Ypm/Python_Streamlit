import re
from lxml import etree

import import_path as imp

imp.import_path("service")
from service import google_translate_service as gt

def lxml(xml_content):
    root = etree.fromstring(xml_content)
    res = root.xpath('.//title')

    return res

## 時間を計算する
def calculate_time(parent_offset, offset, parent_start, duration):
    start = get_time(parent_offset) + get_time(offset) - get_time(parent_start)
    end = start + get_time(duration)
    return start, end

## 親要素の情報を取得する
def get_parent_info(parent):
    if parent is None:
        return None
    return parent.get('offset'), parent.get('start')

## text-styleの情報を取得する text_styleが、Noneの場合があるので、その場合は"None"を返す
def get_text_style(text_styles):
    return next((text_style.text for text_style in text_styles if text_style.text is not None), "None")

## 文字列から秒数を取得する
def get_time(input_str):
    if not input_str:
        return 0
    
    match = re.search(r'(\d+)/?(\d*)s', input_str)
    if match:
        numerator = int(match.group(1))
        denominator = int(match.group(2)) if match.group(2) else 1
        return numerator / denominator
    
    match = re.search(r'(\d+)s', input_str)
    if match:
        return int(match.group(1))
    
    return 0

## 正規表現を使って文字列を検索する
def reg_serach(reg, input_str):
    return re.search(reg, input_str)

## 秒数を時間:分:秒,ミリ秒に変換する
def to_hms_ms(t):
    decimal = 0
    if t > 0:
        decimal = t - int(t)
    t = int(t)
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60

    return f"{zp(h)}:{zp(m)}:{zp(s)},{zp(round(decimal * 1000), 3)}"

## 数値を指定した桁数になるように0埋めする
def zp(num, length=2):
    return str(num).zfill(length)

## 文字処理
def cerate_srt(count, start, end, text):
    return f"{count}\n{start} --> {end}\n{text}\n\n"