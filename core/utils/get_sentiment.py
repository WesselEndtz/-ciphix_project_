import spacy
import asent
import json

def get_sentiment(data, batch_process):
	# load spacy pipeline
	nlp = spacy.blank('en')
	nlp.add_pipe('sentencizer')

	# add the rule-based sentiment model
	nlp.add_pipe('asent_en_v1')
	# if we receive just a string
	if batch_process == False:
		# try an example
		#text = 'I am not very happy, but I am also not especially sad'
		doc = nlp(data)
		# neg=0.0 neu=0.631 pos=0.369 compound=0.7526
		# Naturally, a simple score can be quite unsatisfying, thus Asent implements a series of visualizer to interpret the results:
		#asent.visualize(doc, style='prediction')
		 # or
		#asent.visualize(doc[:5], style='analysis')
		return str(doc._.polarity)
	else:
		#if we receive a list in data
		#we define a returnlist
		sentiment_per_review = []
		# Remove single quotes and whitespace to make it valid JSON
		json_string = data.replace("'", "\"").replace(" ", "")
		# Parse the JSON string to create a Python list
		data = json.loads(json_string)
		#we extract all the strings in the list as text
		for text in data:
			#each string in list gets it's own result in sentiment_per_review
			doc = nlp(text)
			sentiment_per_review.append(str(doc._.polarity))
		# format = [neg=0.0 neu=0.631 pos=0.369 compound=0.7526, neg=0.0 neu=0.631 pos=0.369 compound=0.7526]
		return sentiment_per_review