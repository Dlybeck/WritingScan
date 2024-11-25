import os
from dotenv import load_dotenv
import anthropic
from pathlib import Path

# Input Vars
IMAGE_PATH = "./Sentence.jpg"
SYS_PROMPT_PATH = './gptSys2.txt'
PROMPT = "What does this say?"

# Load environment variables
load_dotenv()

def claude_with_image(image_path, system_prompt):

    # Initialize anthropic (Claude) client
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_KEY"))


    message = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=1000,
        temperature=0,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "data": Path(__file__).parent.joinpath(image_path),
                            "media_type": "image/jpeg"
                        }
                    }#,
                    # {
                    #     "type": "text",
                    #     "text": PROMPT
                    # }
                ]
            }
        ]
    )
    return message.content[0].text



def run_claude(img_path):
    with open(SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        system_prompt = ''.join(lines)
    
    result = claude_with_image(img_path, system_prompt)
    print(result)


run_claude(IMAGE_PATH)