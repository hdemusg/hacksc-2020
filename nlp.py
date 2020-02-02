# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
import json
import requests

def text_sentiments():

	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/HackSC-2020-45a6e91a7f35.json"

# Instantiates a client

	fo=open("xyz.txt", "r")
	print ("Name of the file: ", fo.name)
	lines=[]

	input1="A"
	d={}
	req={}

	while not input1=="":
		input1=fo.readline()
		lines.append(input1)
	for element in lines:
		d = {
		"type": "PLAIN_TEXT",
		"language" : "en",
		"content": element
		}
		data=json.dumps(d)
		with open("document.json", "w") as f:
			f.write(data)

		req = {
		"document" : "document.json",
		"encodingType" : "UTF32"

		}
		sentiment=json.dumps(req)
		with open("analyzeEntitySentiment.json", "w") as f:
			f.write(sentiment)

		url = 'https://language.googleapis.com/v1/documents:analyzeEntitySentiment'
	
		print(sentiment)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
		r = requests.post(url, sentiment)	
	
		output=json.load(r)
		print (output)
		print (element + " " + "Magnitude*Score: " + output["magnitude"]*output["score"])
		print(output["type"])







	client = language.LanguageServiceClient()

# The text to analyze
	text = "xyz.txt"
	document = types.Document(
    	content=text,
    	type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment

	print('Text: {}'.format(text))
	print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))