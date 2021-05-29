from pydantic import BaseModel
from typing import List, Dict


class _Codes(BaseModel):
    full_code : str
    code_alpha_1 : str

class LangSerializer(BaseModel):
    result : List[_Codes]