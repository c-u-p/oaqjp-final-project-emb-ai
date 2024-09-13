import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    emotion_scores = {
        'anger' : formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust' : formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear' : formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy' : formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness' : formatted_response['emotionPredictions'][0]['emotion']['sadness']
    }
    max_score = max(emotion_scores.values())
    dominant_emotion = ''
    for key in emotion_scores:
        if emotion_scores[key] == max_score:
            dominant_emotion = key
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
        }
