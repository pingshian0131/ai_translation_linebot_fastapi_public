from openai import OpenAI

from app.settings import settings


def get_gpt_response(user_text: str, mode: int) -> (str, int, int):
    if mode == settings.TW2EN:
        client = OpenAI(api_key=settings.TW2EN_OPENAI_API_KEY)
        instruction = (
            "Translate the following text from Traditional Chinese to English."
        )
    else:
        client = OpenAI(api_key=settings.EN2TW_OPENAI_API_KEY)
        instruction = (
            "Translate the following text from English to Traditional Chinese."
        )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": instruction,
            },
            {"role": "user", "content": user_text},
        ],
    )
    return (
        response.choices[0].message.content,
        response.usage.prompt_tokens,
        response.usage.completion_tokens,
    )
