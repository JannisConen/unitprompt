import { ChatOpenAI } from "@langchain/openai";
import { StringOutputParser } from "@langchain/core/output_parsers";
import {
    PromptTemplate,
} from "@langchain/core/prompts";

export class LLM {
    model: ChatOpenAI;

    constructor() {
        this.model = new ChatOpenAI({ model: "gpt-4o"});
    }

    public async invoke(prompt: string, variables: any): Promise<any> {
        const promptTemplate = PromptTemplate.fromTemplate(prompt);
        const formattedPrompt = await promptTemplate.format(variables);

        const chain = this.model.pipe(new StringOutputParser());
        return await chain.invoke(formattedPrompt);
    }
}