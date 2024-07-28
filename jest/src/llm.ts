import { ChatOpenAI } from "@langchain/openai";

export class LLM {
    model: ChatOpenAI;

    constructor() {
        this.model = new ChatOpenAI({ model: "gpt-4o" });
    }
}