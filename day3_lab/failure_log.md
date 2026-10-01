# Day 3 Failure Log

## 1. Repeating loop / missing file

Question:

Read fees.html and tell me the fee for CS101.

Result:

The agent called `read_webpage` once. The file did not exist, and the model correctly stopped and reported the missing file.

Observed steps: 1

Conclusion:

The repeating-loop failure did not reproduce with the model used in this experiment.

---

## 2. Hallucinated tool call

A `send_email` tool was mentioned in the system prompt, but it was not actually available in `TOOL_FUNCTIONS`.

Result:

The model did not attempt to call `send_email` in this run.

The code also safely uses:

`TOOL_FUNCTIONS.get(name)`

so an unknown tool would be handled instead of causing a KeyError.

Conclusion:

The hallucinated-tool failure did not reproduce with the model used in this experiment.

---

## 3. Context overflow

File:

big.html

File size:

357,068 characters

The webpage reader was temporarily changed to allow up to 200,000 characters.

Result:

The API returned:

Error 413 - Request too large

Requested: 44,638 tokens

Limit: 8,000 tokens

Conclusion:

The unguarded agent could send too much data to the model, causing a request-size failure.

---

## 4. Fixed agent

The fixed agent added:

- Repeat detection
- Tool-output truncation
- Character budget
- Safe unknown-tool handling

When `big.html` was tested with the fixed agent, the agent eventually stopped with:

`Stopped: repeated tool call detected`

Conclusion:

The fixed agent prevented the uncontrolled tool loop from continuing indefinitely.