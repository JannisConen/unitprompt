import pytest
from unitprompt import assert_fulfills

@pytest.mark.asyncio
async def test_fulfills():
    await assert_fulfills("3", "what is 1 + 2?")
    pass