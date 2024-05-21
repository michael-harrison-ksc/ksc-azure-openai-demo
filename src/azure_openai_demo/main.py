"""
Azure OpenAI Python Documentation:
https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python
"""
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

if __name__ == '__main__':
    load_dotenv()

    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-01",
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        )


    # Send a completion call to generate an answer
    deployment_name= "hackathon_gpt_4"
    message = 'Please return the coordinates of the minimum of the following function: `y=x^2+3x+2`. Explain the steps in your reasoning.'
    response = client.chat.completions.create(model=deployment_name, messages=[{"role": "user", "content": message}])
    print(message)
    print(response.choices[0].message.content)
