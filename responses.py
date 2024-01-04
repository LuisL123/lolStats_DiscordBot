import lolrequests

# Converts the API's request into a readable string.
def handle_response(message) -> str:
    
    summonerName = message['summonerName']
    tier = message['tier']
    rank = message['rank']
    wins = message['wins']
    losses = message['losses']
    winrate = round((wins * 100) / (wins + losses), 1)

    result = f"{summonerName} stats:\ntier: {tier}\nrank: {rank}\nwinrate: {winrate} ({wins} wins and {losses} losses)"
    return result
