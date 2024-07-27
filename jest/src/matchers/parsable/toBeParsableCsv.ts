import { parse } from 'csv-parse/sync';

export function toBeParsableCsv(received: string) {
    try {
        parse(received);
        return {
            message: () => `expected ${received} not to be parsable CSV`,
            pass: true,
        };
    } catch (e) {
        return {
            message: () => `expected ${received} to be parsable CSV`,
            pass: false,
        };
    }
}