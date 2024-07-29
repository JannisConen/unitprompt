
import pytest
from unitprompt.llm import LLM
from unitprompt.utils.get_prompt import get_prompt

async def assert_conciseness(received: str):
    llm = LLM()
    llm.model.max_tokens = 1
    
    result = await llm.invoke(get_prompt("concise"), {"received": received})
    if result == "1":
        pass
    else:
        raise pytest.fail(f"Expected {received} to be concise, but it was not")
    
async def assert_concise_answer(received: str, question: str):
    llm = LLM()
    llm.model.max_tokens = 1
    
    result = await llm.invoke(get_prompt("concise_answer"), {"received": received, "question": question})
    print("RESULT:", result)
    if result == "1":
        pass
    else:
        raise pytest.fail(f"Expected {received} to be a concise answer to {question}, but it was not")