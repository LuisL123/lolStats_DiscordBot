# Discord League Stats Bot

## Description 
This Discord bot is designed to fetch and display League of Legends player statistics in Discord servers. Upon receiving commands in the format @<username>#<server>, the bot queries the Riot Games API to retrieve specific player data, such as tier, rank, and winrate. Built with Python, it uses Discord and Riot Games APIs to provide a user-friendly interface for gamers to access stats without leaving Discord. The bot ensures secure handling of API keys and smooth integration with Discord's messaging features. Feel free to modify the bot to your liking!

## Features
* **Dynamic Commands**: Users can request stats by simply typing @<username>#<server>, making it easy and intuitive.
* **User-Friendly Responses**: Formats the fetched data into easy-to-read messages within Discord.
* **Customizable**: Offers options for customization to server admins, such as command prefixes or response formats.

## Limitations
* The bot's functionality is reliant on the availability of Riot's API, specifically the Summoner-v4 and League-v4 endpoints. These endpoints must be operational for the bot to retrieve and display League of Legends player statistics.
* Requires the server administrator to be constantly updating the API keys to be able to make the requests.

## Installation
1. **Clone this Repository**: Use `https://github.com/LuisL123/lolStats_DiscordBot.git` to clone this extension's code to your local machine.
2. **Invite the Bot to the Server**:
   - Access `https://discord.com/api/oauth2/authorize?client_id=1187410434425364591&permissions=68608&scope=bot` on a webpage.
   - Select the desired server.
   - Click `Authorize`.
3. **Set Up your API keys**:
   - Obtain your Riot Games API key from the Riot Developer Portal at `https://developer.riotgames.com/`. Remember, this key expires every 24 hours and needs to be regenerated for continued use.
   - Paste the API key in the RIOT_API_KEY variable in the `config.py` file.
  
## Usage
1. **Run the Bot**: Execute your bot script (e.g., python `main.py`) to start the bot. It should now be active and responding to commands in your Discord server.
2. **Enjoy!**: Try typing in the server a message in the format @<username>#server and see what the bot responds.

## Contributing
Feel free to modify the code to add any capabilities that you want to the bot. Any improvements and feedback is welcome!

   
