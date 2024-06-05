import requests

def hotels(msg_received):
    location = msg_received["location"]
    
    headers = {"accept": "application/json"}

    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key=6CEC94210D824D8A955CCAF256AC9D48&searchQuery={location}&category=hotels&language=en"
    response = requests.get(url, headers=headers)
    locationId = response['location_id']
    img_url = f"https://api.content.tripadvisor.com/api/v1/location/{locationId}/photos?language=en&key=6CEC94210D824D8A955CCAF256AC9D48"
    img_response = requests.get(img_url, headers=headers)
    img = img_response['data']['images']

    return response


def restaurants(msg_received):
    location = msg_received["location"]

    headers = {"accept": "application/json"}

    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key=6CEC94210D824D8A955CCAF256AC9D48&searchQuery={location}&category=hotels&language=en"
    response = requests.get(url, headers=headers)

    return response