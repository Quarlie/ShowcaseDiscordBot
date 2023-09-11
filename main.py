import os
import asyncio

import datetime as DT

from my_utils import rgb, r
import interactions

#####################
# Various Variables #
#####################


botToken = "xxx"

bot = interactions.Client(token=botToken, intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGE_TYPING | interactions.Intents.GUILD_MEMBERS, fetch_members=True)

bot.red = 0xED4245



bot.botID = 989609470147579904 # self bot ID
bot.modID = 903616174938542111 # mod Role ID
bot.adminID = 903617000201392198 # admin role ID
bot.ownerID = 895674378619060285 # Owner ID
bot.QuarlieID = 430050846999314443 # ME

bot.cleverChannelID = 995263877010968676 # Cleverbot chatting channel
bot.cleverselfChannelID = 993229487636496524 # unused for now, same as cleverbot chatting channel but chats with himself
bot.modbotID = 934138665624563732 # Staff Bots channel ID
bot.modlogsID = 1150144056937152592 # Bot Logs channel ID
bot.serverID = 903601277596999700 # Server ID

bot.path = os.path.dirname(os.path.abspath(__file__)) + "/"

bot.modbot = 0
bot.modlogs = 0
bot.server = 0

#######
# Run #
#######

def main():

    print(f"{rgb(30,230,160)}Loading cogs...{r}")
    for cogDir in os.listdir("./cogs"):
        for filename in os.listdir(f"./cogs/{cogDir}"):
            if filename.endswith(".py"):
                bot.load_extension(f"cogs.{cogDir}.{filename[:-3]}")
                print(f"{rgb(40,150,220)}{filename} Loaded!{r}")
    print(f"{rgb(30,230,160)}Done!{r}")

    bot.start(botToken)



if __name__ == "__main__":
    main()