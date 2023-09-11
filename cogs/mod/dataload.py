import interactions as i
from my_utils import loadDatabase


class Dataload(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="dataload",
        description="boop",
    )
    async def dataload(self, ctx: i.SlashContext):
        await ctx.defer()
        await loadDatabase(self.client)
        await ctx.send("Successfully loaded database!", ephemeral=True)