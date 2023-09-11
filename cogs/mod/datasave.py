import interactions as i
from my_utils import saveDatabase


class Datasave(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="datasave",
        description="boop",
    )
    async def datasave(self, ctx: i.SlashContext):
        await ctx.defer()
        await saveDatabase(self.client)
        await ctx.send("Successfully saved database!", ephemeral=True)