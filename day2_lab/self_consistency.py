import sys
from pathlib import Path
from collections import Counter
from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "day1_lab"))

from config import GROQ_API_KEY, MODEL
from cot_compare import COT_PROMPT, QUESTIONS

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

RUNS = 5
TEMPERATURE = 0.8

def final_answer(text):
    for line in reversed(text.splitlines()):
        if "final answer" in line.lower():
            return line.split(":", 1)[-1].strip()
    return text.splitlines()[-1].strip()

question = QUESTIONS[0]

print("=" * 72)
print("SELF-CONSISTENCY")
print("=" * 72)
print("\nQUESTION:")
print(question)

answers = []

for i in range(1, RUNS + 1):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": COT_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=TEMPERATURE
    )

    answer = final_answer(response.choices[0].message.content)
    answers.append(answer)

    print(f"\nRun {i}: {answer}")

winner, count = Counter(answers).most_common(1)[0]

print("\n" + "=" * 72)
print(f"Majority answer: {winner}")
print(f"Votes: {count}/{RUNS}")