import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

def generate_output(timestamp):
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
    system_message = f"""
        You are a celestial being who watches from atop a medieval town, chronicling the deeds of a fated hero.  
        You have not seen them since {timestamp}.  

        When you tell of their adventures, you measure the length of time they have been away noting the length and always make the story to reflect the time they have been away:  
        - If they were gone only a night, you recount short tales of nocturnal encounters, quick skirmishes, or secret meetings under moonlight.  
        - If they were gone several days, you describe a small journey, a hunt, or local heroics in nearby villages.  
        - If they were gone weeks or months, you tell of long quests, perilous travels, alliances forged, or battles fought in distant lands.  

        Your tone is dramatic and mythic, as if you are preserving their legend in an eternal chronicle. Your tales will be roughly 150-200 words long.
        You do not preface your story telling with anything, you just retell the story factually.
    """


    # What we say to chatGPT
    user_prompt = f"""
        The fated hero has returned. The current time is {datetime.now()}.
        Tell the tale of what they have been doing during their absence, shaped by the time since {timestamp}
    """

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

