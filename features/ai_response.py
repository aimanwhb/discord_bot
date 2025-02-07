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


# def split_message(content, max_length=2000):
#     """Split a message into chunks of max_length characters."""
#     return [content[i:i + max_length] for i in range(0, len(content), max_length)]

def split_message(content, max_length=2000):
    chunks = []
    current_chunk = []
    current_length = 0
    in_code_block = False
    code_block_delimiter = "```"

    for line in content.split('\n'):
        line_stripped = line.strip()
        line_length = len(line) + 1  # +1 for newline

        # Track code block state
        if line_stripped.startswith(code_block_delimiter):
            in_code_block = not in_code_block

        # Check if adding this line would exceed the limit
        if current_length + line_length > max_length:
            if in_code_block:
                # Close the code block before splitting
                current_chunk.append(code_block_delimiter)
                chunks.append("\n".join(current_chunk))
                # Re-open the code block in the next chunk
                current_chunk = [code_block_delimiter, line]
                current_length = len(code_block_delimiter) + line_length + 2
            else:
                # Split normally
                chunks.append("\n".join(current_chunk))
                current_chunk = [line]
                current_length = line_length
        else:
            current_chunk.append(line)
            current_length += line_length

    # Add the final chunk
    if current_chunk:
        if in_code_block:
            current_chunk.append(code_block_delimiter)  # Close any open code blocks
        chunks.append("\n".join(current_chunk))

    # Final check for edge cases (e.g., single lines exceeding max_length)
    final_chunks = []
    for chunk in chunks:
        while len(chunk) > max_length:
            split_index = chunk.rfind('\n', 0, max_length)
            if split_index == -1:
                split_index = max_length
            final_chunks.append(chunk[:split_index])
            chunk = chunk[split_index:].lstrip('\n')
        if chunk:
            final_chunks.append(chunk)

    return final_chunks