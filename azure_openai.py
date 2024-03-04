# from dotenv import load_dotenv
import os
import openai

# load_dotenv()
print("Before")
openai.api_type = "azure"
openai.api_base = "https://hackathon-east-us-1.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = "7f0c8762a942441eb5ad3bdd3516e314"

print("Here")
def get_completion_from_messages(system_message, user_message, model="gpt-4-0125-preview", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    
    return response.choices[0].message["content"]

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))