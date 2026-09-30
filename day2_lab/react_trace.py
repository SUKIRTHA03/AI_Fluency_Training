import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "day1_lab"))

from tools import get_course_fee, calculator

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("QUESTION:", QUESTION)
print("\n--- the agent's actions and observations ---")

cs = get_course_fee("CS101")
print(f"Tool: get_course_fee({{'course_code': 'CS101'}}) -> {cs}")

ai = get_course_fee("AI202")
print(f"Tool: get_course_fee({{'course_code': 'AI202'}}) -> {ai}")

ds = get_course_fee("DS303")
print(f"Tool: get_course_fee({{'course_code': 'DS303'}}) -> {ds}")

first = calculator(f"({cs} + {ai}) * 0.9")
print(f"Tool: calculator({{'expression': '({cs} + {ai}) * 0.9'}}) -> {first}")

second = calculator(f"({cs} + {ai} + {ds}) * 0.75")
print(
    f"Tool: calculator({{'expression': '({cs} + {ai} + {ds}) * 0.75'}}) -> {second}"
)

difference = calculator(f"{second} - {first}")
print(
    f"Tool: calculator({{'expression': '{second} - {first}'}}) -> {difference}"
)

if first < second:
    answer = (
        f"CS101 and AI202 with a 10% scholarship cost Rs. {first:.0f}, "
        f"which is Rs. {difference:.0f} cheaper than all three courses "
        f"at Rs. {second:.0f}."
    )
else:
    answer = (
        f"All three courses with a 25% scholarship cost Rs. {second:.0f}, "
        f"which is Rs. {difference:.0f} cheaper."
    )

print("\nFINAL ANSWER:", answer)