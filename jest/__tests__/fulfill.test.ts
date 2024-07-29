import { unitPromptMatchers } from '../src/unitPromptMatchers';

expect.extend(unitPromptMatchers);

test("fulfills", async () => {
    await expect("3").toFulfill("What is 1+2?")
})

test("does not fulfill", async () => {
    await expect("4").not.toFulfill("What is 1+2?")
})