from googletrans import Translator as gt

## Google Translation Service
def google_translation(text, dest='en'):
    return gt().translate(text, dest=dest).text