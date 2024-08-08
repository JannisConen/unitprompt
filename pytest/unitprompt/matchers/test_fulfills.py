import pytest
from unitprompt.llm import LLM

async def assert_fulfills(received: str, prompt: str, goal: str = "true_false"):
    
    complete_prompt = "<Goal>Check whether the input satisfies the condition</Goal>"
    complete_prompt += "<Condition>{prompt}</Condition>"
    complete_prompt += "<Input>{received}</Input>"
    
    llm = LLM()
    
    if goal == "true_false":
        llm.model.max_tokens = 1
        complete_prompt += "<Response>If condition satisfied: 1, if condition is not satisfied: 0</Response>"
        
    result = await llm.invoke(complete_prompt, { "received": received, "prompt": prompt })
    
    if goal == "true_false":
        if result == "1":
            return
        else:
            raise pytest.fail(f"Expected {received} to be result in a test = 1, but it was not")
    else:
        if result == goal:
            return
        else:
            raise pytest.fail(f"Expected {received} to be fulfill condition, but it did not")