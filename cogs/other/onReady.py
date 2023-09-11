import interactions as i
import sys

from my_utils import loadDatabase, rgb, r

class onReady(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client
        
    @i.listen()
    async def on_ready(self):
        bot = self.client

        sys.path.insert(0, bot.path+"cogs/basic")

        bot.server = bot.get_guild(bot.serverID)
        bot.modbot = bot.server.get_channel(bot.modbotID)
        bot.modlogs = bot.server.get_channel(bot.modlogsID)

        
        await loadDatabase(bot)
        
        print(f"{rgb(240, 0,255)}Bot is now online!{r}")
        await bot.modlogs.send("I am now Online uwu")