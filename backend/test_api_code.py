import requests
import json

# Define the URL of your API endpoint
url = 'http://127.0.0.1:8000/contact/'

# Define the data payload as a dictionary
data = {
    'message': 'super positive stuff',
}

# Set the headers for the request
headers = {
    'Content-type': 'application/json'
}

# Convert the data payload to JSON format
json_data = json.dumps(data)

# Make a POST request using requests
response = requests.post(url, data=json_data, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    print('POST request successful!')
    print(response.json())
else:
    print(f'POST request failed with status code: {response.status_code}')
    print(response.text)

