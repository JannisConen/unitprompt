import pytest
from unitprompt.llm import LLM


async def assert_fulfills(received: str, prompt: str, goal: str = "true_false"):
    
    complete_prompt = "\nTo test: {received}" 
    
    llm = LLM()
    
    if goal == "true_false":
        llm.model.max_tokens = 1
        complete_prompt += "\nIf true: respond with 1, if false with 0"
        
    result = await llm.invoke(prompt + "\nTo test: {received} \n If true: respond with 1, if false with 0", { "received": received })
    
    if goal == "true_false":
        if result == "1":
            pass
        else:
            raise pytest.fail(f"Expected {received} to be result in a test = 1, but it was not")
    else:
        if result == goal:
            pass
        else:
            raise pytest.fail(f"Expected {received} to be fulfill condition, but it did not")