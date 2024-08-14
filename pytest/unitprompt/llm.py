from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

class LLM:
    def __init__(self):
        load_dotenv()
        self.model = ChatOpenAI(model="gpt-4o-mini")

    async def invoke(self, prompt: str, variables: dict) -> str:
        prompt_template = PromptTemplate.from_template(prompt)
        
        # Use the model to generate a response
        chain = prompt_template | self.model | StrOutputParser()
        return chain.invoke(variables)
