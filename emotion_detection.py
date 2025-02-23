# Imports
import requests  
import json

# Create emotion_detector function
def emotion_detector(text_to_analyse):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    return formatted_response

    # Extracting sentiment label and score from the response
    ##TO DO

    # Returning a dictionary containing sentiment analysis results
    #TO DO return {'label': label, 'score': score}