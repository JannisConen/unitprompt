import * as yaml from 'js-yaml';

export function toBeParsableYaml(received: string) {
    try {
        yaml.load(received);
        return {
            message: () => `expected ${received} not to be parsable YAML`,
            pass: true,
        };
    } catch (e) {
        return {
            message: () => `expected ${received} to be parsable YAML`,
            pass: false,
        };
    }
}