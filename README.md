# Azure OpenAI Demo Project

## Set Up
### Azure OpenAI Studio
The models we'll run experiments with are hosted on Azure's OpenAI Studio - [here](https://oai.azure.com/portal). (Alternatively, launch the Studio from the Azure resource [here](https://portal.azure.com/#@cloudopsazoutlook.onmicrosoft.com/resource/subscriptions/af331350-dad4-4dff-a29d-005f5115ac38/resourceGroups/WorkStream-AI-ML/providers/Microsoft.CognitiveServices/accounts/koerber-hackathon/overview)).

The available models are listed under the `Models` tab, which shows the versions (or specific checkpoints of those versions) of OpenAI's models can be used.

We access these models via particular deployments of them, listed under `Deployments`. We have set up deployment of the `gpt-35-turbo-16k` & `gpt-4` models -- `hackathon_gpt_35` & `[TBD]` respectively.

You can chat with these models in a chat UI on the chat playground, on the `Chat` tab.

Alternatively, you can query them using the Python SDK -- see hte instructions below to set this up. 

### Python Environment
Instrctions for setting up the Python environment:
* Clone the repo to your local directory:
<br>
  `git clone https://github.com/chriswmercer/ksc-azure-openai-demo.git`
<br><br>
* Change the working directory to this repository:
<br>
  `cd azure-openai-demo`
<br><br>
* Set up a Python virtual environment:
<br>
  `python3 -m venv .venv`
<br><br>
* And activate it:
<br>
   **Windows:** `.\.venv\Scripts\activate`
<br>
   **Linux/MacOS:** `source .venv/bin/activate` 
<br><br>
* Install the requirements
<br>
  `python -m pip install -r requirements.txt`
<br><br>
* Create a file at the top level directory of the repo called `.env`
<br><br>
* Add the following enviroment variables to it:
    ```
    AZURE_OPENAI_ENDPOINT=https://koerber-hackathon.openai.azure.com/
    AZURE_OPENAI_API_KEY=YOUR-API-KEY
    ```
* You should then be able to run the demonstration script, that illusatrates how to query the API for one of the Azure OpenAI deployments. 
<br>
    `python ./src/azure_openai_demo/main.py`