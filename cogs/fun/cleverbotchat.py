import interactions as i
from cleverbot import Cleverbot

class Cleverbotchat(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.listen()
    async def on_message_create(self, message):
        return
        bot = self.client

        if message.channel_id == bot.cleverChannelID and message.author.id != bot.botID:
            cBot = Cleverbot()
            answer = cBot.send(message.content)
            await message.reply(answer, allowed_mentions={0:False})
        
def setup(client):
    Cleverbotchat(client)
