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

    system_message = """
    You are a sage that retells stories of heroes. You are scribing the adventures of a hero in no more than 50 words with the following
    """

    # Here is where we can do some prompt engineering - we are adding to the system message and creating our endpoint as it were.
    # prompt_engineering = """
    # The last 24 hours
    # """

    # We add the prompt engineering to the system message
    # system_message += prompt_engineering


    # We create our user prompt and will add all of these to the payload.
    user_prompt = "Tell the story of the last 24 hours"


    # OpenAI works was trained with a list of messages - system, user, assistant - so using this is most effective

    prompts = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_prompt},
    ]
    # we will get back as we have seen previously an 'assistant' message.
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=prompts, temperature=2
    )
    print(response.choices[0].message.content)
    output = response.choices[0].message.content.replace("\n", "")

    return output

