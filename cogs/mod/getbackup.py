import interactions as i

class Getbackup(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="getbackup",
        description="boop",
    )
    async def getbackup(self, ctx: i.SlashContext):
        await ctx.defer()

        await ctx.send("Command is W.I.P.", ephemeral=True)