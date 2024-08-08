
# unitprompt - Jest

`unitprompt` is a Jest extension that provides custom matchers for unit testing LLM processes. This library helps ensure that your large language model (LLM) outputs are validated correctly in your tests.

## Installation

### With npm:
```sh
npm install --save-dev unitprompt
```

### With yarn:
```sh
yarn add -D unitprompt
```

## Setup

### Create a setup script with the following:

**setup.js**
```javascript
// add all unitprompt matchers
import { unitPromptMatchers } from './unitPromptMatchers';
expect.extend(unitPromptMatchers);

// or just add specific matchers
import { toBeConciseAnswerTo } from 'unitprompt';
expect.extend({ toBeConciseAnswerTo });
```

### Add your setup script to your Jest `setupFilesAfterEnv` configuration.

**package.json**
```json
"jest": {
  "setupFilesAfterEnv": ["./setup.js"]
}
```

For some features that require LLM calls, please install the dev-dependencies of the packages as well and set the environment variable ```sh OPENAI_API_KEY ```

## Examples
```javascript
// easily test whether custom conditions are fulfilled
test("fulfills", async () => {
    await expect("3").toFulfill("What is 1+2?")
})
// test parsability
test('is parsable JSON', () => {
  expect('{"key": "value"}').toBeParsableJson();
  expect('{key: "value"}').not.toBeParsableJson(); // malformed JSON
});
// test the style of an answer
test('should be concise answer', async () => {
    await expect('7').toBeConciseAnswerTo("3+4=?");
    await expect(`
            First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
            This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

            In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
        `).not.toBeConciseAnswerTo("3+4=?");
})
```