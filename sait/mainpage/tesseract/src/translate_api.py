from PIL import Image
import pytesseract
from .image_changer import prepare_image
from .translator import Translator
import uuid
import os
from langdetect import detect
from .langs import Langs
from pathlib import Path


def translate_image(img_src: str, img_name: str, lang_to: str):
    prepared_image = prepare_image(img_src, img_name)                           
    text = pytesseract.image_to_string(Image.open(prepared_image))              
    trantab = str.maketrans(dict.fromkeys('\n'))                                
    cleaned_text = text.translate(trantab)
    print(cleaned_text)
    try:
        detected_lang = detect(cleaned_text)  
    except:
	detected_lang = 'ru'                                  
        return 'На картинке нет текста'
    print(f'------------------{detected_lang}----------------')
    from_lang = get_lang(detected_lang)                                         
    print(f'------------------{from_lang}----------------')         
    translated_text = Translator.translate(from_lang, lang_to, cleaned_text)    
    os.remove(prepared_image)
    print(prepared_image)
    return translated_text


#Get lang format for transalte api
def get_lang(lang):
    langs = Langs.get_langs()
    for i in langs.result:
        if lang == i.code_alpha_1:
            return i.full_code
            
