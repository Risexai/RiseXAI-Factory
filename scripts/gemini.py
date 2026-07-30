import os
import json
from google import genai


client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


def generate_content(idea, duration):

    prompt = f"""
You are the AI content director for RiseXAI YouTube Shorts.

Create a {duration} second viral AI video concept.

Idea:
{idea}

Style:
- Cinematic
- High retention
- Emotional hook
- Detailed visuals
- Suitable for YouTube Shorts

Return ONLY JSON.

Format:

{{
"title":"",
"description":"",
"hashtags":[],
"thumbnail_prompt":"",
"storyboard":[
 {{
 "scene":1,
 "duration":"3 sec",
 "visual":"",
 "camera":"",
 "sound":""
 }}
],
"video_prompts":[],
"image_prompts":[]
}}

"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
