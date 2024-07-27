
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

### CAUTION
`unitprompt` only supports Jest version 27.2.5 and newer. Older versions of Jest are not supported.

### Create a setup script with the following:

**testSetup.js**
```javascript
// add all unitprompt matchers
import * as matchers from 'unitprompt';
expect.extend(matchers);

// or just add specific matchers
import { toBeValidLLMOutput } from 'unitprompt';
expect.extend({ toBeValidLLMOutput });
```

### Add your setup script to your Jest `setupFilesAfterEnv` configuration.

**package.json**
```json
"jest": {
  "setupFilesAfterEnv": ["./testSetup.js"]
}
```

### To automatically extend `expect` with all matchers, you can use
