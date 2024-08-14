# Unitprompt

This library is the start of a collection of useful prompts and tests to bulletproof your LLM application.

It extends popular unit testing frameworks to facilitate maintaining reliable results during LLM application development.

*Currently supported: jest, python (pytest)*

## Installation

[Installation for jest](jest/README.md)
[Installation for pytest](pytest/README.md)

For some features that require LLM calls, set the environment variable ```sh OPENAI_API_KEY ```

## Examples

```javascript
const generatedResult = yourLLMProcess(); // assume it is 3
const question = "What is 1+2?"

test('should be concise answer', async () => {
    await expect(generatedResult).toBeConciseAnswerTo(question);
})
```

## Development

Create a local symlink for the shared/prompts directory:

For jest inside /jest:

*Windows*
```sh
New-Item -ItemType SymbolicLink -Path .\prompts -Target ..\shared\prompts
```
*Unix*
```sh
ln -s ../shared/prompts ./prompts
```

For pytest inside /pytest/unitprompt:

*Windows*
```sh
New-Item -ItemType SymbolicLink -Path .\prompts -Target ..\..\shared\prompts
```
*Unix*
```sh
ln -s ../shared/prompts ./prompts
```
