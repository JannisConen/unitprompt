import { unitPromptMatchers } from '../src/unitPromptMatchers';

expect.extend(unitPromptMatchers);

test('is parsable JSON', () => {
  expect('{"key": "value"}').toBeParsableJson();
  expect('{key: "value"}').not.toBeParsableJson(); // malformed JSON
});

test('should validate YAML strings correctly', () => {
  expect('key: value\nanother_key: another_value').toBeParsableYaml();
  expect('key: value\nanother_key another_value').not.toBeParsableYaml(); // malformed YAML
});

test('should validate XML strings correctly', () => {
  expect('<root><child /></root>').toBeParsableXml();
  expect('<root><child></root>').not.toBeParsableXml(); // malformed XML
});

test('should validate CSV strings correctly', () => {
  expect('name,age\nJohn,30\nDoe,40').toBeParsableCsv();
  expect('name,age\nJohn,30\nDoe').not.toBeParsableCsv(); // malformed CSV
});
