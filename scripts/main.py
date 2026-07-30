import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--idea", required=True)
parser.add_argument("--duration", required=True)

args = parser.parse_args()

output = Path("output")
output.mkdir(exist_ok=True)

with open("output/title.txt","w",encoding="utf-8") as f:
    f.write(
        f"RiseXAI Short: {args.idea}"
    )

with open("output/description.txt","w",encoding="utf-8") as f:
    f.write(
        f"""
RiseXAI AI Video

Idea:
{args.idea}

Duration:
{args.duration} seconds
"""
    )

print("RiseXAI Content Created")
