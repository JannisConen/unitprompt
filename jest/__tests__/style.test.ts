import { unitPromptMatchers } from '../src/unitPromptMatchers';

expect.extend(unitPromptMatchers);

describe('Style Matchers', () => {

    test('should be concise', async () => {
        await expect('3+4=7').toBeConcise();
        await expect(`
            First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
            This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

            In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
        `).not.toBeConcise();
    })

    test('should be concise answer', async () => {
        await expect('7').toBeConciseAnswerTo("3+4=?");
        await expect(`
                First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
                This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

                In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
            `).not.toBeConciseAnswerTo("3+4=?");
    })
});