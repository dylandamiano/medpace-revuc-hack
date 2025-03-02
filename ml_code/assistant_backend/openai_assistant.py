from openai import OpenAI
import toml

toml_creds = toml.load('./settings/credential.toml')
OAI_API_KEY = toml_creds['CREDENTIALS']["OAI_API_KEY"]

OAI_CLIENT_HANDLE: OpenAI = OpenAI(api_key=OAI_API_KEY)


# Probably better off making an object for this but YOLO!
def retrieve_suggestions(disease_level=1, ):
    # Define the prompt
    PROMPT = f"Provide advice on what a patient could do to improve their lifestyle to reduce the risk of developing chronic kidney disease {disease_level}..."

    # Define the completion parameters
    COMPLETION_PARAMS = {
        "temperature": 0.5,
        "max_tokens": 100,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stop": ["\n"]
    }

    # Generate the completion
    response = OAI_CLIENT_HANDLE.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": PROMPT},
        ],
        **COMPLETION_PARAMS
    )

    # Print the completion
    print(response.choices)

retrieve_suggestions(5)