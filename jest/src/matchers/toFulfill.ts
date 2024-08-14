import { LLM } from "../llm";

export async function toFulfill(received: string, prompt: string | string[]) {
    const llm = new LLM();
    const unfulfilledConditions: string[] = [];

    // Ensure prompt is an array
    if (!Array.isArray(prompt)) {
        prompt = [prompt];
    }

    for (const condition of prompt) {
        let completePrompt = "<Goal>Check whether the input satisfies the condition</Goal>";
        completePrompt += `<Condition>{condition}</Condition>`;
        completePrompt += `<Input>{received}</Input>`;
        
        // Limiting maxTokens as it will only expect a "1" or "0" response
        llm.model.maxTokens = 1;
        completePrompt += "<Response>If condition satisfied: 1, if condition is not satisfied: 0</Response>";

        const result = await llm.invoke(completePrompt, { received, condition });

        if (result !== "1") {
            unfulfilledConditions.push(condition);
        }
    }

    if (unfulfilledConditions.length > 0) {
        return {
            message: () => `Expected "${received}" to satisfy the following conditions: ${unfulfilledConditions.join(", ")}, but it did not.`,
            pass: false,
        };
    } else {
        return {
            message: () => `Expected "${received}" to satisfy the given conditions, and it did.`,
            pass: true,
        };
    }
}
