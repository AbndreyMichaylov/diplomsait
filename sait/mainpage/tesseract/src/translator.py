import json
import requests

class Translator:
    _req_url = 'https://api-b2b.backenster.com/b1/api/v3/translate'
    _token = 'a_rhll2FCx8ugHWFTqQzZfYhTpTH7aF0N3VIJxz11lHVINlZCBRcAVuRkoQVvfZcPyLxEu2U5VCOOzqE0S'
    _header = {
        "Authorization" : _token,
        "accept":"application/json",
        "Content-Type":"application/json"
    }

    def translate(from_eng, to_eng, text):
        _data = json.dumps({
            "from": from_eng,
            "to": to_eng,
            "data": text,
            "platform": "api"
        })
        r = requests.post(
            Translator._req_url, 
            headers=Translator._header, 
            data=_data
        )
        return r.json()['result']