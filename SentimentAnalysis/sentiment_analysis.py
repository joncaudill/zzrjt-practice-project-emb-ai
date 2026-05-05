import requests
import json

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # URL of the sentiment analysis service 
    myobj = { "raw_document": { "text": text_to_analyze } } 
    # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 
    # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) 
    # Send a POST request to the API with the text and headers return response.text 
    if response.status_code == 200:
        response_data = json.loads(response.text)
        label = response_data["documentSentiment"]["label"]
        score = response_data["documentSentiment"]["score"]
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
    res = {
        "label": label,
        "score": score,
    }
    return res
    