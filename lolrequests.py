import requests

def get_summoner_id(username, server, api_key):
    url = f"https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['id']
    else:
        # Uncomment for debugging
        # print('Nothing was return from ur request')
        return None
    
def get_ranked_stats(summoner_id, server, api_key):
    url = f"https://{server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
