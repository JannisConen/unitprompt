
# unitprompt

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