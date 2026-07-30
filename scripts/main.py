import argparse
import json
from pathlib import Path

from gemini import generate_content


parser = argparse.ArgumentParser()

parser.add_argument("--idea", required=True)
parser.add_argument("--duration", required=True)

args = parser.parse_args()


output = Path("output")
output.mkdir(exist_ok=True)


print("Generating AI content...")


result = generate_content(
    args.idea,
    args.duration
)


print(result)


data = json.loads(result)


files = {

"title.txt": data["title"],

"description.txt": data["description"],

"hashtags.txt":
"\n".join(data["hashtags"]),

"thumbnail_prompt.txt":
data["thumbnail_prompt"],

"storyboard.json":
json.dumps(
    data["storyboard"],
    indent=2
),

"video_prompts.md":
"\n\n".join(data["video_prompts"]),

"image_prompts.md":
"\n\n".join(data["image_prompts"])

}


for filename, content in files.items():

    with open(
        output / filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


print("RiseXAI AI package completed!")
