import requests
import json
import constants

# Replace 'YOUR_API_KEY' with your actual Steam WebAPI key
API_KEY = constants.steamKey

# Function to get match details by match ID
def get_dota2_mmr(player_id):
    url = f"https://api.opendota.com/api/players/{player_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'mmr_estimate' in data:
            return data['mmr_estimate']['estimate']
        else:
            return "MMR data not found"
    else:
        return "Error fetching data"
