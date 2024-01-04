import discord
import responses
import lolrequests
from config import RIOT_API_KEY, DISCORD_BOT_TOKEN


# async def send_message(message, user_message, is_private):
#     try:
#         response = responses.handle_response(user_message)
#         if response:  # Check if the response is not empty
#             if is_private:
#                 await message.author.send(response)
#             else:
#                 await message.channel.send(response)
#         else:
#             print(f"No response generated for the message: {user_message}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def run_bot():
    Token = DISCORD_BOT_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    # This function let's you know when the bot is running through the terminal.
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        content = message.content
        if content.startswith("@"):
            try:
                username, server = content[1:].split("#")
                api_key = RIOT_API_KEY
            
                summoner_id = lolrequests.get_summoner_id(username, server, api_key)
                if summoner_id:
                    stats = lolrequests.get_ranked_stats(summoner_id, server, api_key)
                    if stats:
                        # Format and send stats
                        await message.channel.send(responses.handle_response((stats)))
                    else:
                        await message.channel.send("Could not retrieve ranked stats.")
                else:
                    await message.channel.send("Summoner not found.")
            except ValueError:
                await message.channel.send("Invalid format. Please use @<username>#<server>")


    client.run(Token)