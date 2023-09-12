import requests
import json

# Define the URL of your API endpoint
url = 'https://ciphixprojectdemo.azurewebsites.net/txt_sentiment/'
url2 = 'http://127.0.0.1:8000/txt_sentiment/'

"""
as 'data' you can either give a regular string or a list, with a list it will
be more efficient by taking the whole list in one api call and returning the
results in list format where data[n] = result[n]
"""

data = ['bad', 'bad', 'good, maybe', 'bad', 'this is a great product']
data = 'maybe this is a bad review'

# Create a dictionary with a key-value pair where the key represents the data
json_data = {"message": data}
# Convert the data payload to JSON format
json_data = json.dumps(json_data)

# Set the headers for the request
headers = {
    'Content-type': 'application/json'
}

# Make a POST request using requests
response = requests.post(url2, data=json_data, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    print('POST request successful!')
    print(response.json())
else:
    print(f'POST request failed with status code: {response.status_code}')
    print(response.text)

