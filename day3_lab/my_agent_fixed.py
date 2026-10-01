import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "day1_lab"))

from openai import OpenAI
from config import GROQ_API_KEY, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS
from my_agent import SYSTEM_PROMPT

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MAX_TOOL_CHARS = 1500
CHAR_BUDGET = 30000


def agent(question, max_steps=6, verbose=True):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    seen_calls = {}
    chars_sent = 0

    for step in range(1, max_steps + 1):

        current_chars = sum(
            len(str(message.get("content", "")))
            for message in messages
        )

        chars_sent += current_chars

        if chars_sent > CHAR_BUDGET:
            return "Stopped: character budget exceeded."

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:
            name = call.function.name
            arguments = {}

            try:
                arguments = json.loads(
                    call.function.arguments or "{}"
                )

                signature = (
                    name,
                    json.dumps(arguments, sort_keys=True)
                )

                seen_calls[signature] = seen_calls.get(signature, 0) + 1

                if seen_calls[signature] >= 3:
                    return (
                        f"Stopped: repeated tool call detected: "
                        f"{name}({arguments})"
                    )

                function = TOOL_FUNCTIONS.get(name)

                if function is None:
                    result = (
                        f"Unknown tool: {name}. "
                        f"Available: {list(TOOL_FUNCTIONS)}"
                    )
                else:
                    result = function(**arguments)

            except json.JSONDecodeError as error:
                result = f"Argument error: {error}. Send valid JSON."

            except TypeError as error:
                result = f"Argument error: {error}"

            result = str(result)

            if len(result) > MAX_TOOL_CHARS:
                result = (
                    result[:MAX_TOOL_CHARS]
                    + " ... [tool output truncated]"
                )

            if verbose:
                print(
                    f"   step {step}: {name}({arguments}) "
                    f"-> {result[:120]}"
                )

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":
    print("=" * 60)
    print("MY AGENT (fixed)")
    print("=" * 60)

    question = "Read big.html and tell me how many students are listed."
    print("Q:", question)
    print("A:", agent(question))