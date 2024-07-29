import fs from "fs";
import path from "path";

const getPrompt = (promptFilename: string): string => {
    const promptPath = path.join(__dirname, '../../prompts', `${promptFilename}.txt`);
    return fs.readFileSync(promptPath, 'utf8');
}

export { getPrompt };