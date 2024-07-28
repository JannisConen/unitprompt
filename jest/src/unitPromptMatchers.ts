import { toBeParsableCsv } from "./matchers/parsable/toBeParsableCsv";
import { toBeParsableJson } from "./matchers/parsable/toBeParsableJson";
import { toBeParsableXml } from "./matchers/parsable/toBeParsableXml";
import { toBeParsableYaml } from "./matchers/parsable/toBeParsableYaml";
import { toBeConcise, toBeConciseAnswerTo } from "./matchers/style/toBeConcise";
import { toUseHtml } from "./matchers/uses/toUseHtml";
import { toUseLatex } from "./matchers/uses/toUseLatex";
import { toUseMarkdown } from "./matchers/uses/toUseMarkdown";
import dotenv from 'dotenv';

dotenv.config();

interface UnitPromptMatchers<R = unknown> {
    toBeParsableJson(): R;
    toBeParsableXml(): R;
    toBeParsableYaml(): R;
    toBeParsableCsv(): R;
    toUseHtml(): R;
    toUseLatex(): R;
    toUseMarkdown(): R;
    toBeConcise(): Promise<R>;
    toBeConciseAnswerTo(question: string): Promise<R>;
  }
  
  declare global {
    namespace jest {
      interface Matchers<R> extends UnitPromptMatchers<R> {}
    }
  }
  
  export const unitPromptMatchers: jest.ExpectExtendMap = {
    toBeParsableJson,
    toBeParsableXml,
    toBeParsableYaml,
    toBeParsableCsv,
    toUseHtml,
    toUseLatex,
    toUseMarkdown,
    toBeConcise,
    toBeConciseAnswerTo,
  };
  