import requests

# Constants
# Headers with Authorization token
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Payload for creating an image pin
payload = {
    'board_id': BOARD_ID,
    'image_url': IMAGE_URL,
    'title': PIN_TITLE,
    'description': PIN_DESCRIPTION,
    'link': PIN_LINK
}

# Making the POST request to create an image pin
response = requests.post(PIN_CREATE_URL, headers=headers, json=payload)

# Checking response status
if response.status_code == 201:
    print('Image pin created successfully!')
    print(response.json())
else:
    print('Failed to create pin.')
    print(response.status_code, response.text)
