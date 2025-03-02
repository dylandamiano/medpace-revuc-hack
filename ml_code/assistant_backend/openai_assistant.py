from openai import OpenAI
import toml

toml_creds = toml.load('credential.toml')
OAI_API_KEY = toml_creds['CREDENTIALS']["OAI_API_KEY"]

OAI_CLIENT_HANDLE: OpenAI = OpenAI(api_key=OAI_API_KEY)


# Probably better off making an object for this but YOLO!
def retrieve_suggestions(disease_level, age, wc, sod, bp, gfr, sc, bfr, pot):
    # Define the prompt
    PROMPT = f"Provide advice on what a patient could do to improve their lifestyle to reduce the risk of developing chronic kidney disease stage {disease_level}; given the following variables age: {age}, wc: {wc}, sod: {sod}, bp: {bp}, sc: {sc}, bfr: {bfr}, pot: {pot}, gfr: {gfr}..." + "(as JSON form for bulletpoints for upstream processing with the following format: {'steps': [...]})"

    # Generate the completion
    response = OAI_CLIENT_HANDLE.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": PROMPT},
        ],
    )

    # Print the completion
    return response.choices[0].message.content