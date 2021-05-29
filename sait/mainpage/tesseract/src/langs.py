from .Serializers.langs_serializer import LangSerializer

class Langs:
    serializer = LangSerializer

    def get_langs():
        with open(r'C:\Users\cjcbc\Desktop\diplom_sait\sait\mainpage\tesseract\src\langs_list.json', 'r' , encoding='utf-8') as langs:
            data = LangSerializer.parse_raw(langs.read())
            return data