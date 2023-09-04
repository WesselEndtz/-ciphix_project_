# Project documentation

## Installation guide

We assume you have git installed on your computer

#### step 1 : clone git
```bash
clone git_url
```

#### step 2 : open git on terminal
```bash
cd git_name
```

#### step 3 : create a virtual env using
```bash
python -m venv env_name
```
(env_name = name, best practise name = "venv", since that is ignored in .gitignore)

#### step 4 : activate the venv
```bash
source env_name/bin/activate
```

#### step 5 : install packages
```bash
pip install -r requirements.txt
```

## Usage guide

Python script
```python
import requests
import json

# Define the URL of your API endpoint
url = 'http://yoururl.com/txt_sentiment/'

#add your text you want to analyse here
text_to_analyse = 'super positive stuff'

# Define the data payload as a dictionary
data = {
    'message': text_to_analyse,
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
```