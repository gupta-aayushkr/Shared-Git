import requests

# Constants
ACCESS_TOKEN = '45d824fdd808831cacc4b185a3c5832d3922179c'
PIN_CREATE_URL = 'https://api.pinterest.com/v5/pins'
BOARD_ID = 'PFP'
IMAGE_URL = 'https://www.pfpgeeks.com/static/images/anime-girl-pfp/webp/anime-girl-38.webp'
PIN_TITLE = 'Anime Girl PFP'
PIN_DESCRIPTION = 'Anime Girl PFP'
PIN_LINK = 'https://www.pfpgeeks.com/static/images/anime-girl-pfp/webp/anime-girl-38.webp'

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
