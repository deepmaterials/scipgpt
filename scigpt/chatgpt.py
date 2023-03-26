import os
import openai


openai.api_key = os.environ["OPENAI_API_KEY"]


def get_response(
    text="Tell the world about the ChatGPT API in the style of a pirate.",
    API_KEY="",
):
    """Get ChtGPT response."""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}]
    )

    return completion.choices[0].message.content


resp = get_response(API_KEY=API_KEY)
print(resp)
