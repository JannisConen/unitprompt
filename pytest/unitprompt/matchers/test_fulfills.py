import pytest
from unitprompt.llm import LLM
import logging

logger = logging.getLogger(__name__)

async def assert_fulfills(received: str, prompt: str, goal: str = "true_false"):
    
    complete_prompt = "This is the result of a function: {received}\n#\n Check if this condition is 100% fulfilled: {prompt}"
    
    llm = LLM()
    
    if goal == "true_false":
        llm.model.max_tokens = 1
        complete_prompt += "\n#\n<Your response>If condition fulfilled: respond with 1, if not with 0</Your response>"
        
    result = await llm.invoke(complete_prompt, { "received": received, "prompt": prompt })
    
    logger.info(f"Result: {result}")
    
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