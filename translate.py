from googletrans import Translator
def trans(text):
    translator = Translator()
    return (str(translator.translate(text, dest='ru'))).split('dest=ru, text=')[1].split(', pronun')[0]