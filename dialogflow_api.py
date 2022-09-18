import os
import configparser
from google.cloud import dialogflow

directory = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(f"{directory}/config.ini")

PROJECT_ID = str(config.get("dialogflow","project_id"))
SESSION_ID = "123456789"
KEY_PATH = "./dialogflow_api.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=KEY_PATH

def send_message_diagflow(input_text:str):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)

    text_input = dialogflow.TextInput(text=input_text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    
    intent_name = response.query_result.intent.display_name
    if intent_name in ["jokes.get","jokes.get.more","jokes.feedback.bad","jokes.feedback.good"]:
        full_res_text = response.query_result.fulfillment_messages[2].text.text[0]

    else:
        full_res_text=""
        for m in response.query_result.fulfillment_messages:
            full_res_text += m.text.text[0]+" "

    return {
    "question": response.query_result.query_text,
    "intent": response.query_result.intent.display_name,
    "response": full_res_text
    }