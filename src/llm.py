from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import get_settings
from prompts import PROMPT_TEMPLATE
from parsers import get_project_parser, CharacterTemplate

SETTINGS = get_settings()

class LLMService:
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            model=SETTINGS.model, openai_api_key=SETTINGS.openai_key
        )
        print("Starting llm")
        self.parser = get_project_parser()
        self.prompt_template = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["origen", "felicidad", "tristeza", "sorpresa", "enojo"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )

    def generate(self, origen, felicidad, tristeza, sorpresa, enojo) -> CharacterTemplate:
        _input = self.prompt_template.format_prompt(origen=origen, felicidad=felicidad, tristeza=tristeza, sorpresa=sorpresa, enojo=enojo)
        output = self.llm.predict(_input)
        return self.parser.parse(output)                                                                  

