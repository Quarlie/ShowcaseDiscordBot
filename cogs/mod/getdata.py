import interactions as i

class Getdata(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="getdata",
        description="boop",
    )
    async def getdata(self, ctx: i.SlashContext):
        await ctx.defer()

        await ctx.send("Command is W.I.P.", ephemeral=True)