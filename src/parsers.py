from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class CharacterTemplate(BaseModel):
    origen: str
    objetivos: str

def get_project_parser():
    return PydanticOutputParser(pydantic_object=CharacterTemplate)