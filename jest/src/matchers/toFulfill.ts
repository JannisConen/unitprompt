import { LLM } from "../llm";

export type FulfillmentGoal = "true_false" | string

export async function toFulfill(received: string, prompt: string, goal: FulfillmentGoal = "true_false") {
    
    const llm = new LLM();

    prompt += "\nTo test: {received}";

    if (goal == "true_false"){
        llm.model.maxTokens = 1;
        prompt += "\nIf true: respond with 1, if false with 0";
    }

    const result = await llm.invoke(prompt, { received: received });

    if (goal == "true_false"){

        if (result === "1") {
            return {
                message: () => `expected ${received} to fulfill ${goal}`,
                pass: true,
            };
        } else {
            return {
                message: () => `expected ${received} not to fulfill ${goal}`,
                pass: false,
            };
        }
    } else {
        if (result == goal) {
            return {
                message: () => `expected ${received} to fulfill ${goal}`,
                pass: true,
            };
        } else {
            return {
                message: () => `expected ${received} not to fulfill ${goal}`,
                pass: false,
            };
        }
    }
}