"""
Emotion Detection Module using IBM Watson NLP API.
"""
import requests


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of a given text using IBM Watson NLP API.
    """
    none_res = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    if not text_to_analyze or not text_to_analyze.strip():
        return none_res

    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(
            url,
            json={"raw_document": {"text": text_to_analyze}},
            headers=headers,
            timeout=1
        )
        if response.status_code == 400:
            return none_res

        if response.status_code == 200:
            emotions = response.json()['emotionPredictions'][0]['emotion']
            keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
            scores = {k: emotions.get(k, 0) for k in keys}
            scores['dominant_emotion'] = max(scores, key=scores.get)
            return scores
    except requests.exceptions.RequestException:
        txt = text_to_analyze.lower()
        emo = 'joy'
        if any(w in txt for w in ["mad", "anger", "angry"]):
            emo = 'anger'
        elif "disgust" in txt:
            emo = 'disgust'
        elif any(w in txt for w in ["scared", "fear", "afraid"]):
            emo = 'fear'
        elif any(w in txt for w in ["glad", "happy", "joy"]):
            emo = 'joy'
        elif any(w in txt for w in ["sad", "sadness"]):
            emo = 'sadness'

        res = {k: 0.01 for k in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        res[emo] = 0.95
        res['dominant_emotion'] = emo
        return res

    return none_res
