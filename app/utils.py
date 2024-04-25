import os
from groq import Groq

def groq_helper(prompt, **kwargs):

    groq_api_key = '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'
    os.environ["GROQ_API_KEY"] = groq_api_key
        
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    role = kwargs.get('role', 'user')
    modelid = kwargs.get('modelid', 'mixtral-8x7b-32768')
    temperature = kwargs.get('temperature', 0.7)
    top_p = kwargs.get('top_p', 1.0)
    max_tokens = kwargs.get('max_tokens', 500)
    stop_sequences = kwargs.get('stop_sequences', None)
    stream = kwargs.get('stream', False)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": role,
                "content": prompt,
            }
        ],
        model=modelid,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stop=stop_sequences,
        stream=stream
    )

    print(chat_completion.choices[0].message.content)
    print(kwargs)


