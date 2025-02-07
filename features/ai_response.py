import os
import json
import requests

def get_ai_response(query: str) -> str:

    try:
        response = requests.post(
            url=os.environ.get("AI_ENDPOINT"),
            headers={
                "Authorization": f"Bearer {os.environ.get("AI_TOKEN")}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": os.environ.get("AI_MODEL"),
                "messages": [
                    {
                        "role": "user",
                        "content": f"{query}"
                    }
                ],
                # "max_tokens": 3500,
            })
        )
        # return response.json()["choices"][0]["message"]["content"].strip().replace("\n", "")
        content = response.json()["choices"][0]["message"]["content"].strip()
        return content

    except Exception as e:
        return f"Sorry, I couldn't process your request. Error: {str(e)}"


def split_message(content, max_length=2000):
    """Split a message into chunks of max_length characters."""
    return [content[i:i + max_length] for i in range(0, len(content), max_length)]
