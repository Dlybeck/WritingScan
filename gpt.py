from dotenv import load_dotenv
from openai import OpenAI
import base64


# Define the prompt and image path
IMAGE_PATH = "./Sentence.jpg"
#SYS_PROMPT_PATH = 'gptSys.txt'
SYS_PROMPT_PATH = 'gptSys2.txt'
PROMPT = "What does this say?"


# Load environment variables
load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def chatgpt_with_image(image_path, system_prompt):
    client = OpenAI()

    # Getting the base64 string
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        model="gpt-4o",
        
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": system_prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )
    
    return response.choices[0].message.content

def run_chatgpt(img_path):
    with open(SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        system_prompt = ''.join(lines)
    
    result = chatgpt_with_image(img_path, system_prompt)
    print(result)

# # Read the system prompt from a file
# with open(SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     system_prompt = ''.join(lines)

# result = chatgpt_with_image(IMAGE_PATH)

# print(result)