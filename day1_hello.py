# day1_hello.py
# Run inside GitHub Codespaces. Reads OPENAI_API_KEY from the environment.

from openai import OpenAI           # 1) Import the official OpenAI client
import os                           # 2) Lets us read environment variables

api_key = os.getenv("OPENAI_API_KEY")  # 3) Get your key from the environment
if not api_key:                        # 4) If missing, stop with a clear message
    raise RuntimeError(
        "OPENAI_API_KEY is not set. In GitHub, go to: "
        "Repo → Settings → Secrets and variables → Codespaces → New secret "
        "Name: OPENAI_API_KEY, Value: sk-... Then reopen the Codespace."
    )

client = OpenAI(api_key=api_key)    # 5) Create the OpenAI client using your key

# 6) Send a simple chat request (this is your 'task')
response = client.chat.completions.create(
    model="gpt-4o-mini",            # 7) Small, fast model for testing
    messages=[
        {"role": "system", "content": "You are a helpful tutor."},
        {"role": "user", "content": "Explain AI tools in 2 sentences."}
    ]
)

# 8) Print the model's text reply
print(response.choices[0].message.content)
