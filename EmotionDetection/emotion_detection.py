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

    # Error handling
    # 400 bad request 
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else: #if not bad request
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # Store contents of 'emotion' in dictionary index 0 as 'emotions' variable
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Get max score (dominant emotion)
        dominant_emotion = max(emotions, key=emotions.get)

        # Return emotion scores and dominant emotion
        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }