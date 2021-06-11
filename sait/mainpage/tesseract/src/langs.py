from .Serializers.langs_serializer import LangSerializer
from django.conf import settings

class Langs:
    serializer = LangSerializer

    def get_langs():
        with open(settings.JSONDEPLOYPATH, 'r' , encoding='utf-8') as langs:
            data = LangSerializer.parse_raw(langs.read())
            return data
