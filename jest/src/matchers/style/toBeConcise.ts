import { LLM } from "../../llm";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { getPrompt } from "../../utils/getPrompt";

export async function toBeConcise(received: string){

    const llm = new LLM();
    llm.model.maxTokens = 1;

    const result = await llm.invoke(getPrompt("concise"), { received });

    if (result === "1") {
        return {
            message: () => `expected ${received} not to be concise`,
            pass: true,
        };
    } else {
        return {
            message: () => `expected ${received} to be concise`,
            pass: false,
        };
    }
}

export async function toBeConciseAnswerTo(received: string, question: string){
    
    const llm = new LLM();
    llm.model.maxTokens = 1;

    const result = await llm.invoke(getPrompt("concise_answer"), { received, question });

    if (result === "1") {
        return {
            message: () => `expected ${received} not to be concise answer`,
            pass: true,
        };
    } else {
        return {
            message: () => `expected ${received} to be concise answer`,
            pass: false,
        };
    }
}