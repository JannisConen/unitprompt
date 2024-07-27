import { JSDOM } from 'jsdom';

export function toBeParsableXml(received: string) {
    try {
        const dom = new JSDOM();
        const parser = new dom.window.DOMParser();
        const parsedDoc = parser.parseFromString(received, "application/xml");
        const parseError = parsedDoc.getElementsByTagName("parsererror");

        if (parseError.length > 0) {
            throw new Error('Parsing error');
        }

        return {
            message: () => `expected ${received} not to be parsable XML`,
            pass: true,
        };
    } catch (e) {
        return {
            message: () => `expected ${received} to be parsable XML`,
            pass: false,
        };
    }
}