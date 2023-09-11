import os
import interactions as i

from my_utils import rgb, r

class Reload(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="reload",
        description="boop"
    )

    async def reload(self, ctx: i.SlashContext):
        bot = self.client
        await ctx.defer()

        print(f"{rgb(30, 230, 160)}Reloading cogs...{r}")
        for cogDir in os.listdir("./cogs"):
            for filename in os.listdir(f"./cogs/{cogDir}"):
                if filename.endswith(".py"):
                    bot.load_extension(f"cogs.{cogDir}.{filename[:-3]}")
                    print(f"{rgb(40, 150, 220)}{filename} Reloaded!{r}")
        print(f"{rgb(30, 230, 160)}Done!{r}")

        await ctx.send("Successfully Reloaded!")
