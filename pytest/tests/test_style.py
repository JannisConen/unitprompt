import pytest
from unitprompt.matchers.style.test_conciseness import assert_concise_answer, assert_conciseness

@pytest.mark.asyncio
async def test_conciseness():
    await assert_conciseness("3+4=7")
    
@pytest.mark.asyncio
async def test_conciseness_fail():
    
    long_text = """
    First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
    This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

    In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
    """
    
    with pytest.raises(pytest.fail.Exception):
        await assert_conciseness(long_text)

@pytest.mark.asyncio
async def test_concise_answer():
    await assert_concise_answer("7", "What is 3+4?")
    
@pytest.mark.asyncio
async def test_concise_answer_fail():
    # Test a non-concise answer
    long_answer = """
    First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
    This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

    In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
    """
    with pytest.raises(pytest.fail.Exception):
        await assert_concise_answer(long_answer, "3+4=?")