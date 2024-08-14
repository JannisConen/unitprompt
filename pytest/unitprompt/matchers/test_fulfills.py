import pytest
from unitprompt.llm import LLM

async def assert_fulfills(received: str, prompt):
    
    # Check if prompt is a list, if not, convert it to a list
    if not isinstance(prompt, list):
        prompt = [prompt]
    
    llm = LLM()
    
    unfulfilled_conditions = []
    for condition in prompt:
        complete_prompt = "<Goal>Check whether the input satisfies the condition</Goal>"
        complete_prompt += "<Condition>{condition}</Condition>"
        complete_prompt += "<Input>{received}</Input>"
        
        llm.model.max_tokens = 1
        complete_prompt += "<Response>If condition satisfied: 1, if condition is not satisfied: 0</Response>"
            
        result = await llm.invoke(complete_prompt, { "received": received, "condition": condition })
        
        if result != "1":
            unfulfilled_conditions.append(condition)

    if len(unfulfilled_conditions) > 0:
        raise pytest.fail(f"Expected {received} to satisfy the following conditions: {unfulfilled_conditions}, but it did not.")