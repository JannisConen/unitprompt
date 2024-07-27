export function toBeParsableJson(received: string) {
    try {
        JSON.parse(received);
        return {
            message: () => `expected ${received} not to be parsable JSON`,
            pass: true,
        };
    } catch (e) {
        return {
            message: () => `expected ${received} to be parsable JSON`,
            pass: false,
        };
    }
}