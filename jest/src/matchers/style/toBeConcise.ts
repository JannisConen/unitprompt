import { LLM } from "../../llm";
import { StringOutputParser } from "@langchain/core/output_parsers";

export async function toBeConcise(received: string){
    
    const model = new LLM().model;
    model.maxTokens = 1;
    const chain = new LLM().model.pipe(new StringOutputParser());

    const result = await chain.invoke("You have to decide whether the following text is concise. If it is concise, return a 1, else a 0. Text:\n" + received)

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
    
    const model = new LLM().model;
    model.maxTokens = 1;
    const chain = new LLM().model.pipe(new StringOutputParser());

    const result = await chain.invoke("You have to decide whether the following text is a concise answer to the question. If it is concise, return a 1, else a 0. Question:\n" + question + "\n Text:\n" + received)

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