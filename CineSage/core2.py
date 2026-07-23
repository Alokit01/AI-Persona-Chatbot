from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

from langchain_mistralai import ChatMistralAI 
model=ChatMistralAI(model="mistral-medium-3-5") #using model code not in_itchat model

class Movie(BaseModel):
    title:str
    release_year:int
    genre:List[str]
    director:str
    cast:List[str]
    rating:Optional[float]
    summary:str

parser=PydanticOutputParser(pydantic_object=Movie)
prompt=ChatPromptTemplate.from_messages([
    ('system', """
Extract movie information from the paragraph
{format_information}'
""" ),(
    "human","{paragraph}"
)]
)
para=input("Give Your Paragraph")
final_prompt=prompt.invoke({"paragraph":para,
                            'format_instruction': parser.get_format_instructions})
response=model.invoke(final_prompt)
print(response.content)