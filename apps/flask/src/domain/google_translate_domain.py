from googletrans import Translator

translator = Translator()

# テキストを指定した言語から別の言語に翻訳する
translated_text = translator.translate('Hello, how are you?', dest='ja')

print(translated_text.text)

def reslt():
    return translated_text.text