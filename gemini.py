from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Define the prompt and image path
IMAGE_PATH = "./Sentence.jpg"
SYS_PROMPT_PATH = 'gptSys.txt'
PROMPT = "What does this say?"


# Load environment variables
load_dotenv()

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

def gemini_with_image(image_path, system_prompt):
    myfile = genai.upload_file(image_path)
    print(f"{myfile=}")

    model = genai.GenerativeModel("gemini-1.5-pro")
    result = model.generate_content(
        [myfile, "\n\n", system_prompt]
    )
    return f"{result.text=}"

def run_gemini(img_path):
    with open(SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        system_prompt = ''.join(lines)
    
    result = gemini_with_image(img_path, system_prompt)
    print(result)
    

result = run_gemini(IMAGE_PATH)
