import os
from dotenv import load_dotenv
from openai import OpenAI

def generate_output(user_prompt):
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY"),
        )
    
    if GROQ_API_KEY:
        print(f"GROQ_API_KEY exists and begins {GROQ_API_KEY[:14]}...")
    else:
        print("GROQ_API_KEY not set")

    # The context in which chatGPT will respond
    system_message = """
    You are a sage that retells stories of heroes. You are retelling the adventures of a hero in no more than 50 words
    """


    # What we say to chatGPT
    user_prompt = "Tell the story of the last 24 hours"

    prompts = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=prompts, temperature=2
    )
    print(response.choices[0].message.content)
    output = response.choices[0].message.content.replace("\n", "")

    return output

