import requests

def tourist_sites(msg_received):
    location = msg_received["location"]
    
    headers = {"accept": "application/json"}

    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key=6CEC94210D824D8A955CCAF256AC9D48&searchQuery={location}&category=attractions&language=en"
    response = requests.get(url, headers=headers)

    return response


def geos(msg_received):
    location = msg_received["location"]
    headers = {"accept": "application/json"}

    url = f"https://api.content.tripadvisor.com/api/v1/location/search?key=6CEC94210D824D8A955CCAF256AC9D48&searchQuery={location}&category=geos&language=en"
    response = requests.get(url, headers=headers)

    return response