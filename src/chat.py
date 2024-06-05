from openai import OpenAI

from .settings import settings

client = OpenAI(base_url=settings.llm_api_url, api_key=settings.llm_api_key)

history = [
    {
        "role": "system",
        "content": f"You are an intelligent assistant called {settings.bot_name}. You always provide well-reasoned answers that are both correct and helpful.",
    },
]


def ask_bot(message: any) -> str:
    history.append(
        {
            "role": "user",
            "content": message if isinstance(message, str) else message.text,
        }
    )

    completion = client.chat.completions.create(
        model=settings.llm_model,
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            # print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    return new_message["content"]
